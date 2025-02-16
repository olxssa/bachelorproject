import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from imageio.v2 import imread
from skimage.filters import gaussian
from skimage.measure import find_contours, label, regionprops_table, regionprops, perimeter
from skimage.morphology import dilation, disk
from scipy.ndimage import binary_fill_holes
import pandas as pd
import skfmm # distance field package
import csv
from knockdown_nrs import knockdown_nrs
import skimage
from scipy.signal import argrelextrema
from compute_curvature import compute_real_curvature_values

path = '/Users/olyssa/Desktop/BA_data/'

def get_object_mask(img, gaussian_sigma=5, dilation_disk_size=3, th=0.005):

   if gaussian_sigma is not None:
      img_f = gaussian(img, gaussian_sigma)
   else:
      img_f = img

   img_b = np.where(img_f > th, 1, 0).astype(bool)
   if dilation_disk_size is not None:
      img_b = dilation(img_b, disk(dilation_disk_size))

   mask = label(img_b)

   return  mask

def fill_boundary_object(mask):

   for l in np.unique(mask):

      if l == 0: continue
      object_mask = np.where(mask == l, 1, 0)

      lower_bounds = np.argwhere(np.diff(object_mask[-1, :]))
      if len(lower_bounds) > 0:
         lower_bounds = np.min(lower_bounds), np.max(lower_bounds)
         # print(l,lower_bounds)
         mask[-1, lower_bounds[0]:lower_bounds[1]] = l

      upper_bounds = np.argwhere(np.diff(object_mask[0, :]))
      if len(upper_bounds) > 0:
         upper_bounds = np.min(upper_bounds), np.max(upper_bounds)
         mask[0, upper_bounds[0]:upper_bounds[1]] = l

      left_bounds = np.argwhere(np.diff(object_mask[:, 0]))
      if len(left_bounds) > 0:
         left_bounds = np.min(left_bounds), np.max(left_bounds)
         mask[left_bounds[0]:left_bounds[1],0] = l

      right_bounds = np.argwhere(np.diff(object_mask[:, -1]))
      if len(right_bounds) > 0:
         right_bounds = np.min(right_bounds), np.max(right_bounds)
         mask[right_bounds[0]:right_bounds[1], -1] = l

      return mask

def get_contour_dataframe(rp, mask):
   contours = []
   for l in rp.label:
      filled_mask = binary_fill_holes(np.where(mask == l, 1, 0))
      c = find_contours(filled_mask, 0)
      for cc in c:
         contours.append({"curve": cc, "parent_object": l, "length": len(cc)})

   contours = pd.DataFrame(contours)

   return contours

def get_minimum_distance_field(mask): # for feature extraction: KeyError: 'length'

   distance_fields = []
   for l in np.unique(mask):
      if l == 0: continue

      d = skfmm.distance(binary_fill_holes(np.where(mask == l, 1, 0)))
      d = np.where(mask == l, d, np.nan)
      distance_fields.append(d)
   d = np.nanmin(np.array(distance_fields), axis=0)
   return d

def get_border_coords(img, cell_layers_included=5, cell_diam=16):
    x_shift = cell_layers_included * cell_diam

    mask = get_object_mask(img)
    mask = fill_boundary_object(mask)
    rp = pd.DataFrame(regionprops_table(mask, properties=["label", "area"]))
    rp = rp.sort_values("area", ascending=False).iloc[:2] # only take the two biggest areas
    mask = np.where(np.isin(mask, rp.label), mask, 0)
    c = find_contours(binary_fill_holes(mask))

    c2 = []
    for i, con in enumerate(c):
       if i in list(np.argsort([len(c) for c in c], )[-2:]):
          c2.append(con)

    scratch_border_right = [c2[1][:, 1], c2[1][:, 0]]
    border_right = [c2[1][:, 1] + x_shift, c2[1][:, 0]]
    border_left = [c2[0][:, 1] - x_shift, c2[0][:, 0]]
    scratch_border_left = [c2[0][:, 1], c2[0][:, 0]]

    return border_left, scratch_border_left, scratch_border_right, border_right

# Define polygons: polygons_borders, polygons_bulk, polygon_scratch
def create_polygon_scratch(img):
    border_left, scratch_border_left, scratch_border_right, border_right = get_border_coords(img)

    x = [*scratch_border_left[0][::-1], *scratch_border_right[0][::-1]]
    y = [*scratch_border_left[1][::-1], *scratch_border_right[1][::-1]]

    coords = []

    for i in range(len(x)):
        coords.append((x[i], y[i]))
    polygon = Polygon(coords)

    return polygon

def create_polygons_borders(img):
    border_left, scratch_border_left, scratch_border_right, border_right = get_border_coords(img)

    x_left = [*border_left[0], *scratch_border_left[0][::-1]]
    y_left = [*border_left[1], *scratch_border_left[1][::-1]]
    x_right = [*border_right[0], *scratch_border_right[0][::-1]]
    y_right = [*border_right[1], *scratch_border_right[1][::-1]]
    coords_left = []

    for i in range(len(x_left)):
        coords_left.append((x_left[i], y_left[i]))
    # coords_left = np.where(coords_left[:, 0] > 0, coords_left)
    polygon_left = Polygon(coords_left)
    coords_right = []

    for i in range(len(x_right)):
        coords_right.append((x_right[i], y_right[i]))
    # coords_right = np.where(coords_right[:, 0] < 1770, coords_right)
    polygon_right = Polygon(coords_right)

    return polygon_left, polygon_right


def create_polygons_bulk(img):
    border_left, scratch_border_left, scratch_border_right, border_right = get_border_coords(img, cell_layers_included=20)

    x_left = [0, 0, *border_left[0][::-1]]
    y_left = [0, np.max(border_left[1]), *border_left[1][::-1]]
    x_right = [1772, 1772, *border_right[0]]
    y_right = [0, np.max(border_right[1]), *border_right[1]]

    coords_left = []
    for i in range(len(x_left)):
       coords_left.append((x_left[i], y_left[i]))
    polygon_left = Polygon(coords_left)

    coords_right = []
    for i in range(len(x_right)):
       coords_right.append((x_right[i], y_right[i]))
    polygon_right = Polygon(coords_right)

    return polygon_left, polygon_right

def get_cell_features(t, img, mask):
    img_intensity = img
    cell_features = skimage.measure.regionprops_table(mask, img_intensity,
                                                      properties=['label',
                                                                  'centroid',
                                                                  'area',
                                                                  'area_bbox',
                                                                  'bbox',
                                                                  'area_convex',
                                                                  'axis_major_length',
                                                                  'axis_minor_length',
                                                                  'eccentricity',
                                                                  'equivalent_diameter_area',
                                                                  'extent',
                                                                  'feret_diameter_max',
                                                                  'orientation',
                                                                  'perimeter',
                                                                  'perimeter_crofton',
                                                                  'solidity'
                                                                  ]
                                                      )
    return t, cell_features

def add_extra_properties(mask):
    array_convexity = []
    array_form_factor = []
    array_circularity = []
    array_aspect_ratio = []
    array_perimeter_curl = []
    array_roundness = []
    array_inscribed_area = []
    array_sphericity = []
    array_curl = []
    array_concavity = []
    array_protrusion = []

    labeled_img, count = label(mask, return_num=True)
    props = regionprops(labeled_img)

    for i in range(np.max(labeled_img)):
        perim = props[i].perimeter
        area = props[i].area
        axis_major = props[i].axis_major_length
        axis_minor = props[i].axis_minor_length
        convex_hull = props[i].image_convex
        convex_hull = np.array(convex_hull)
        perim_convex_hull = perimeter(convex_hull)
        maski = (mask == i).astype(int)
        real_curvature_values = compute_real_curvature_values(maski, 20, 5)
        max_inscribed_radius = axis_minor * 0.5
        fiber_length = props[i].feret_diameter_max

        # 0
        try:
            convexity = perim / perim_convex_hull
        except ZeroDivisionError:
            convexity = 0

        # 1
        try:
            form_factor = area / perim ** 2
        except ZeroDivisionError:
            form_factor = 0

        # 2
        try:
            circularity = 4 * np.pi * area / perim ** 2
        except ZeroDivisionError:
            circularity = 0

        # 3
        try:
            aspect_ratio = axis_major / axis_minor
        except ZeroDivisionError:
            aspect_ratio = 0

        # 4
        try:
            perimeter_curl = perim / np.pi * (1 - np.sqrt(1 - 4 * np.pi * area / perim ** 2))
        except ZeroDivisionError:
            perimeter_curl = 0

        # 5
        try:
            roundness = 4 * np.pi * area / perim_convex_hull ** 2
        except ZeroDivisionError:
            roundness = 0

        # 6
        try:
            inscribed_area = axis_major ** 2 * np.pi / max_inscribed_radius
        except ZeroDivisionError:
            inscribed_area = 0

        # 7
        try:
            sphericity = 2 * max_inscribed_radius / axis_major
        except ZeroDivisionError:
            sphericity = 0

        # 8
        try:
            curl = axis_major/fiber_length
        except ZeroDivisionError:
            curl = 0

        # 9
        try:
            concavity = ((len((np.where(np.sign(real_curvature_values[:-1]) != np.sign(real_curvature_values[1:]))[
                                   0] + 1))) /
                         len(real_curvature_values))
        except ZeroDivisionError:
            concavity = 0 # np.nan

        # 10
        try:
            protrusion = len(argrelextrema(real_curvature_values, np.greater, order=5)[0])
        except ZeroDivisionError:
            protrusion = 0

        array_convexity.append(convexity) # 0
        array_form_factor.append(form_factor) # 1
        array_circularity.append(circularity) # 2
        array_aspect_ratio.append(aspect_ratio) # 3
        array_perimeter_curl.append(perimeter_curl) # 4
        array_roundness.append(roundness) # 5
        array_inscribed_area.append(inscribed_area) # 6
        array_sphericity.append(sphericity) # 7
        array_curl.append(curl) # 8
        array_concavity.append(concavity) # 9
        array_protrusion.append(protrusion) # 10

    return [array_convexity, # 0
            array_form_factor, # 1
            array_circularity, # 2
            array_aspect_ratio, # 3
            array_perimeter_curl, # 4
            array_roundness, # 5
            array_inscribed_area, # 6
            array_sphericity, # 7
            array_curl, # 8
            array_concavity, # 9
            array_protrusion] # 10

def add_feature_columns(exp_nr, knockdown_nr, t, img, df_data):

    centroids = [] # for polygons
    centroids_arr = [] # for distance field

    for i in range(len(df_data)):
        y_coord = df_data['centroid-0'][i]
        x_coord = df_data['centroid-1'][i]
        centroids.append(Point(x_coord, y_coord))
        centroids_arr.append([y_coord, x_coord])

    try:
        # Inside scratch
        polygon_scratch = create_polygon_scratch(img)
        df_data['inside_scratch'] = polygon_scratch.contains(centroids)

        # At borders of scratch with cell_layers_included=5
        polygon_border_left, polygon_border_right = create_polygons_borders(img)
        df_data['at_border_left'] = polygon_border_left.contains(centroids)
        df_data['at_border_right'] = polygon_border_right.contains(centroids)

        # Inside bulk with cell_layers_included=20
        polygon_bulk_left, polygon_bulk_right = create_polygons_bulk(img)
        df_data['bulk_left'] = polygon_bulk_left.contains(centroids)
        df_data['bulk_right'] = polygon_bulk_right.contains(centroids)

    except IndexError:
        new_row = [['exp_nr: ', exp_nr, 'knockdown_nr: ', knockdown_nr, 'timepoint: ', t]]
        with open('/home/basar/Olyssa/feature_tables/add_features_log.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_row)
        pass

    try:
        # Distance field values
        mask_d = get_object_mask(img)
        mask_d = fill_boundary_object(mask_d)
        rp = pd.DataFrame(regionprops_table(mask_d, properties=["label", "area"]))
        rp = rp.sort_values("area", ascending=False)
        mask_d = np.where(np.isin(mask_d, rp.label), mask_d, 0)
        distance_field = get_minimum_distance_field(mask_d)

        centroids_arr = np.around(centroids_arr, decimals=0).astype(int)
        df_data['distance_field'] = distance_field[centroids_arr[:, 0], centroids_arr[:, 1]]
    except ValueError:
        new_row = [['exp_nr: ', exp_nr, 'knockdown_nr: ', knockdown_nr, 'timepoint: ', t]]
        with open('/home/basar/Olyssa/feature_tables/distance_field_log.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_row)
        pass

    return df_data
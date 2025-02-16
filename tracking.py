import pandas as pd
import matplotlib.pyplot as plt
from skimage.measure import regionprops_table
import numpy as np
def create_whole_tracks(y_tracked):
    rps = []
    for t, mask in enumerate(y_tracked[:, :, :, 0]):
        rp = pd.DataFrame(regionprops_table(mask, properties=["label", "centroid"]))
        rp["time"] = t
        rps.append(rp)
    df = pd.concat(rps)
    df = df.rename(columns={"centroid-0": "ycol", "centroid-1": "xcol"})

    # create dataframe for each timepoint
    df_0 = df[df['time'] == 0]
    df_1 = df[df['time'] == 1]
    df_2 = df[df['time'] == 2]
    df_3 = df[df['time'] == 3]
    df_4 = df[df['time'] == 4]
    df_5 = df[df['time'] == 5]
    df_6 = df[df['time'] == 6]
    df_7 = df[df['time'] == 7]
    df_8 = df[df['time'] == 8]
    df_9 = df[df['time'] == 9]
    df_10 = df[df['time'] == 10]
    df_11 = df[df['time'] == 11]
    df_12 = df[df['time'] == 12]
    df_13 = df[df['time'] == 13]
    df_14 = df[df['time'] == 14]
    df_15 = df[df['time'] == 15]
    df_16 = df[df['time'] == 16]

    # rename y- and x-position
    df_0 = df_0.rename({'ycol': f'y_0', 'xcol': f'x_0'}, axis=1)
    df_1 = df_1.rename({'ycol': f'y_1', 'xcol': f'x_1'}, axis=1)
    df_2 = df_2.rename({'ycol': f'y_2', 'xcol': f'x_2'}, axis=1)
    df_3 = df_3.rename({'ycol': f'y_3', 'xcol': f'x_3'}, axis=1)
    df_4 = df_4.rename({'ycol': f'y_4', 'xcol': f'x_4'}, axis=1)
    df_5 = df_5.rename({'ycol': f'y_5', 'xcol': f'x_5'}, axis=1)
    df_6 = df_6.rename({'ycol': f'y_6', 'xcol': f'x_6'}, axis=1)
    df_7 = df_7.rename({'ycol': f'y_7', 'xcol': f'x_7'}, axis=1)
    df_8 = df_8.rename({'ycol': f'y_8', 'xcol': f'x_8'}, axis=1)
    df_9 = df_9.rename({'ycol': f'y_9', 'xcol': f'x_9'}, axis=1)
    df_10 = df_10.rename({'ycol': f'y_10', 'xcol': f'x_10'}, axis=1)
    df_11 = df_11.rename({'ycol': f'y_11', 'xcol': f'x_11'}, axis=1)
    df_12 = df_12.rename({'ycol': f'y_12', 'xcol': f'x_12'}, axis=1)
    df_13 = df_13.rename({'ycol': f'y_13', 'xcol': f'x_13'}, axis=1)
    df_14 = df_14.rename({'ycol': f'y_14', 'xcol': f'x_14'}, axis=1)
    df_15 = df_15.rename({'ycol': f'y_15', 'xcol': f'x_15'}, axis=1)
    df_16 = df_16.rename({'ycol': f'y_16', 'xcol': f'x_16'}, axis=1)

    # drop column time
    df_0 = df_0.drop('time', axis=1)
    df_1 = df_1.drop('time', axis=1)
    df_2 = df_2.drop('time', axis=1)
    df_3 = df_3.drop('time', axis=1)
    df_4 = df_4.drop('time', axis=1)
    df_5 = df_5.drop('time', axis=1)
    df_6 = df_6.drop('time', axis=1)
    df_7 = df_7.drop('time', axis=1)
    df_8 = df_8.drop('time', axis=1)
    df_9 = df_9.drop('time', axis=1)
    df_10 = df_10.drop('time', axis=1)
    df_11 = df_11.drop('time', axis=1)
    df_12 = df_12.drop('time', axis=1)
    df_13 = df_13.drop('time', axis=1)
    df_14 = df_14.drop('time', axis=1)
    df_15 = df_15.drop('time', axis=1)
    df_16 = df_16.drop('time', axis=1)

    # merge all
    df_merged = df_0.merge(df_1, on="label")
    df_merged = df_merged.merge(df_2, on='label')
    df_merged = df_merged.merge(df_3, on='label')
    df_merged = df_merged.merge(df_4, on='label')
    df_merged = df_merged.merge(df_5, on='label')
    df_merged = df_merged.merge(df_6, on='label')
    df_merged = df_merged.merge(df_7, on='label')
    df_merged = df_merged.merge(df_8, on='label')
    df_merged = df_merged.merge(df_9, on='label')
    df_merged = df_merged.merge(df_10, on='label')
    df_merged = df_merged.merge(df_11, on='label')
    df_merged = df_merged.merge(df_12, on='label')
    df_merged = df_merged.merge(df_13, on='label')
    df_merged = df_merged.merge(df_14, on='label')
    df_merged = df_merged.merge(df_15, on='label')
    df_merged = df_merged.merge(df_16, on='label')

    return df_merged, df

# Plot cell movements: t=0 (green), t=17 (blue)
regions = [
    (1430, 238, 130, 200),
    (390, 281, 130, 200)
]
def plot_cell_movements(df_merged, stack):
    fig, ax = plt.subplots(figsize=(20.6, 6))
    plt.imshow(stack[0], cmap='Greys_r')
    for i in range(len(df_merged)):
        cell = df_merged.loc[i]
        cell = np.delete(cell, 0)
        cell_y = cell[::2]
        cell_x = cell[1::2]
        plt.plot(cell_x, cell_y, color='red', linewidth=2, zorder=0)
        plt.scatter(cell_x[0], cell_y[0], s=150, c='limegreen', marker='x', linewidth=4, zorder=1)
        plt.scatter(cell_x[-1], cell_y[-1], s=150, c='blue', marker='x', linewidth=4, zorder=1)
    ax.text(10, 480, f'x', color="limegreen", fontsize=40, weight="bold")
    ax.text(40, 480, f' = start ', color="black", fontsize=40)
    ax.text(300, 480, f'x', color="blue", fontsize=40, weight="bold")
    ax.text(320, 480, f' = end', color="black", fontsize=40)
    ax.text(550, 480, f'—', color="red", fontsize=40, weight="bold")
    ax.text(590, 480, f' = trajectory', color="black", fontsize=40)
    ax.set_axis_off()
    plt.tight_layout()

    plt.show()

def create_data_list(df_merged):
    arr_merged = np.array(df_merged)
    df_list_data = pd.DataFrame()
    df_list_data['t'] = list(range(17))
    list_data = []
    for i in range(len(arr_merged)):
        y = arr_merged[i][1::2]
        x = arr_merged[i][2::2]
        t = np.array(list(range(17)))
        track = np.array([t, x, y])
        list_data.append(track)
    return list_data
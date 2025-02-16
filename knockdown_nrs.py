knockdown_nrs = []
for i in range(1, 10):
    for k in range(1, 10):
        knockdown_nrs.append(f'00{i}00{k}')
for i in range(10, 17):
    for k in range(1, 10):
        knockdown_nrs.append(f'0{i}00{k}')
for i in range(1, 10):
    for k in range(10, 25):
        knockdown_nrs.append(f'00{i}0{k}')
for i in range(10, 17):
    for k in range(10, 25):
        knockdown_nrs.append(f'0{i}0{k}')
knockdown_nrs.sort()


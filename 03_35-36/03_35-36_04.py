def transforming(matrix, *conditions, not_transform=(), **kwargs):
    for condition in conditions:
        func_name, indexes = condition
        if func_name not in not_transform:
            func = kwargs.get(func_name, lambda x: x)
            for i, j in indexes:
                matrix[i][j] = func(matrix[i][j])
    return matrix


data = [
    [12, 13, 5, 7, 8, 24],
    [101, 5, 1, 9, 6, 32],
    [-5, 3, 3, -2, 8, -11]
]

data = transforming(
    data,
    ('comb', (2, 5)),
    ('near5', (0, 3)),
    ('abracodabra', (0, 3)),
    ('binary', (1, 0)),
    ('make_odd', (1, 4)),
    not_transform=('comb',),
    near5=lambda x: x + 2 if x < 5 else x - 2,
    comb=lambda x: int(str(x % 100) + str(x // 100)),
    binary=lambda x: int(all([int(i) in (0, 1) for i in str(x)])),
    make_odd=lambda x: x + x % 2 + 1)
print(*data, sep='\n')

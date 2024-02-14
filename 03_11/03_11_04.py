def distance(*args: tuple) -> list:
    result = []
    for i in args:
        d = (i[0] ** 2 + i[1] ** 2) ** (1/2)
        result.append(d)
    return result

points = [
    (0, 1), (1, 0), (1, 1),
    (2, 3), (3, 4), (9, 12)
]
print(*distance(*points), sep='\n')

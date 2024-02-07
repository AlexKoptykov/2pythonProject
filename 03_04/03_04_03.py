def lines_ratio(k1: int, b1: int, k2: int, b2: int) -> int:
    result = 0
    if k1 == k2 and b1 == b2:
        result = 2
    else:
        if k1 == k2 and b1 != b2:
            result = 0
        else:
            result = 1
    return result

verdicts = {
    0: "параллельны",
    1: "пересекаются",
    2: "совпадают"
}

lines = [(1, 2), (1, 3), (2, -2)]

for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        result = lines_ratio(
            lines[i][0], lines[i][1],
            lines[j][0], lines[j][1]
        )
        print(
            lines[i], lines[j],
            verdicts[result]
        )

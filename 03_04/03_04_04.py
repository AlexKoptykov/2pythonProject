def inter_x(k1: int, b1: int, k2: int, b2: int) -> float:


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
        if result == 1:
            x = inter_x(
                lines[i][0], lines[i][1],
                lines[j][0], lines[j][1]
            )
            y = inter_y(
                lines[i][0], lines[i][1],
                lines[j][0], lines[j][1]
            )
            print(f"в точке ({x}, {y})")
        print()

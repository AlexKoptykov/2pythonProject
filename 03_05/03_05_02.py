def print_triangle(lines_number: int) -> None:
    for i in range(lines_number + 1):
        print('*' * i)

for i in range(2, 5):
    print_triangle(i)
    print()

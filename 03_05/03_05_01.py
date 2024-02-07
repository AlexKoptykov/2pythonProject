def odd_numbers(limit: int) -> None:
    for i in range(limit + 1):
        if i % 2 != 0:
            print(i, end=' ')
    print()

odd_numbers(6)
odd_numbers(3)
odd_numbers(10)

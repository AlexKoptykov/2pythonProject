def mult_table(n: int) -> None:
    for i in range(1, n+1):
        for j in range(i, (i * n) + 1, i):
            print(j, end='\t')
        print()


for i in range(1, 5 + 1, 2):
    mult_table(i)
    print()

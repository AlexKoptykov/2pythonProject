def kover(n: int):
    for i in range(n):
        for j in range(n):
            print("# ", end="")
        print()


n = int(input("Введите число: "))
kover(n)

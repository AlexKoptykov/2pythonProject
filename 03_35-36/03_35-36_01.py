def kover_tringl(n):
    n = n - 2
    print("#" * (n + 2))
    for i in range(n):
        print("#", end="")
        for j in range(n):
            if i == j or i == n - j - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print("#")
    print("#" * (n + 2))


n = int(input("Введите число: "))
kover_tringl(n)

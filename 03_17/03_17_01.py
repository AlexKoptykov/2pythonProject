import math


def reducefraction(n, m):
    gcd = math.gcd(n, m)
    n, m = n // gcd, m // gcd
    return (n, m)


n = int(input())
m = int(input())
print(*reducefraction(n, m))

def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def giper(n):
    while n > 10:
        if not(is_prime(n)):
            return 'NO'
        n = n // 10

    return 'YES'


n = int(input())
print(giper(n))

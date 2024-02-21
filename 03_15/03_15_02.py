def is_prime(number: int) -> bool:
    if number == 1:
        return False
    for i in range(2, (number//2)+1):
        if number % i == 0:
            return False
    return True


for i in range(1, 10 + 1):
    if is_prime(i):
        print(i, end=" ")

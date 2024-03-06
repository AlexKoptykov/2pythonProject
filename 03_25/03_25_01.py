num = list(map(float, input("Введите числа через пробел").split()))
print('Yes' if any(map(lambda n: n > 0, num)) else 'No')

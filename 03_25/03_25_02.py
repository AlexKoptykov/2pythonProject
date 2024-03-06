num = list(map(float, input().split()))
print('Yes' if all(map(lambda n: n % 2 == 0, num)) else 'No')

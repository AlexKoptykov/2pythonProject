from sys import stdin

data = stdin.readlines()
print(*data[::-1])

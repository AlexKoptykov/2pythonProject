n = int(input())
f = map(lambda num: int(num) * n, input().split())
print(*list(f))

n, m = map(int, input("Введите размер матрицы: ").split())
matrix = []
t = 0
for _ in range(n):
    r = list(map(int, input().split()))
    matrix.append(r)

for i in matrix:
    t += sum(i)
count = t / (n * m)
black = []

for i in matrix:
    bw_r = [0 if pixel < count else 255 for pixel in i]
    black.append(bw_r)

print(f"{count:.4f}")
for i in black:
    print(*i)

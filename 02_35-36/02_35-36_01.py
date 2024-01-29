m = int(input("Введите размер комнаты: "))
n = int(input("Введите кол-во числовых показателей: "))
maxs = 0
tv_a, tv_b = 0, 0
p = []
for d in range(n):
    pn = int(input("Введите показатели: "))
    p.append(pn)

for i in range(len(p) - 1):
    for j in range(i + 1, len(p)):
        s = p[i] + p[j]
        c = p[i] * p[j]
        if s % m == 0 and c > maxs:
            maxs = c
            tv_a, tv_b = p[i], p[j]

if maxs > 0:
    print(tv_a, tv_b)
else:
    print("0 0")


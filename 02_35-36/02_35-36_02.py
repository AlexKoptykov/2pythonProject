n = int(input("Введите кол-во участников: "))
num = list(input("Введите список номеров, присланные телезрителями: ").split())
count = {}
for i in num:
    if int(i) <= n:
        count[i] = count.get(i, 0) + 1
maxs = max(count.values())
win = [key for key, value in count.items() if value == maxs]

print(*sorted(win))

from sys import stdin

text = stdin.readlines()
count = 0
for i in text:
    count = count + 1
    print(f'Строка {count}: {len(i) - 1} сим.')

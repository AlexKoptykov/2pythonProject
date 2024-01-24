alphabet = input("Введите алфовит ")
line = input("Введите строку ")
frec = dict()
for i in alphabet:
    count = 0
    for j in line:
        if i == j:
            count += 1
    frec[i] = count

for k,v in frec.items():
    print(f'{k} - {v}')
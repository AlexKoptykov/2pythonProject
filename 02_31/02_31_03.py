string = dict()
line = input("Введите строку ").split()
n = int(input("Введите кол-во запросов "))
for i in range(0, n):
    word = input("Введите слово ")
    count = 0
    for j in line:
        if j == word:
            count += 1
    string[word] = count

print(string.values())
for k, v in string.items():
    print(v)

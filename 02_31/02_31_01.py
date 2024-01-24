word = dict()
input_str = input("Введите строку ").split()
for i in input_str:
    if i not in word:
        word[i] = 1
    else:
        word[i] += 1
    print(word[i], end=' ')

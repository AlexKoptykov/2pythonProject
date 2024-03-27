def vol(x):
    vol = 'vol'
    count = 0
    for i in range(0, len(x), 2):
        if x[i] in vol:
            count += 1
    return count


def sort(w):
    w = w.split()
    w.sort(key=lambda x: (vol(x), x.lower()))
    return ' '.join(w).split()


w = input("Введите текст: ")
print(*sort(w), sep="\n")

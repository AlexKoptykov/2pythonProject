old_print = print


def new_print(*args, **kwargs):
    lst = []
    for i in args:
        lst.append(str(i).upper())
    old_print(*lst, **kwargs)


print = new_print
print("Kirill", 132, "привет", sep="\n")

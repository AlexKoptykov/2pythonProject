n = input()
lst = n.split()
lst = list(map(int, lst))
print(lst[0::2])
l1 = input('Список 1 ')
l2 = input('Список 2 ')
lst1 = l1.split()
lst2 = l2.split()
print(l1, lst1)
print(l2, lst2)
lst1.extend(lst2)
print(lst1)
print(*lst1)
data = [("Василий", 13), ("Пётр", 7), ("Евгений", 12), ("Алла", 3)]
names, numbers = [i[0] for i in data], [i[1] for i in data]
print(*names)
print(*numbers)

def find_unique_elements(*args: list) -> list:
    for i in args:
        for j in args:
            if i == j:


first = [1, 2, 3]
second = [2, 3, 4]
third = [3, 4, 5]
print(*find_unique_elements(
first, second, third
))
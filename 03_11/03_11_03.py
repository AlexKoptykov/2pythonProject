def merge_lists(*args: list) -> list:
    result = []
    for i in args:
        result.extend(i)
    return result

first = [1, 2, 3]
second = ["a", "Kirill", 1]
third = []
print(merge_lists(first, second, third))

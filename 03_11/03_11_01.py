def average(*args: int) -> float:
    return sum(args) / len(args)

# print(average(1, 2, 3, 4))
first_average = average(3, 7)
second_average = average(4, 1, -1)
result = first_average + second_average
print(result)

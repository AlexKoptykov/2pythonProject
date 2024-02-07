def is_root(a: int, b: int, c: int, x: int) -> bool:
    result = False # начальное значение ответа
    if a * x * x + b * x * x + c == 0:
        result = True
    return result

a, b, c = 1, 0, -4
for x in range(-3, 3 + 1):
    verdict = "не корень"
    if is_root(a, b, c, x):
        verdict = "корень"
    print(x, verdict)

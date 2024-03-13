def power_series(power):
    def locf(left, right):
        for i in range(left, right + 1):
            print(i**power, end=' ')
        print()
    return locf


f_series = power_series(2)
s_series = power_series(1)
t_series = power_series(3)
f_series(1, 5)
s_series(-2, 2)
t_series(5, 8)

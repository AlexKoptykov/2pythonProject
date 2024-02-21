def f(*args, **kwargs):
    while kwargs:

    return args


data = ['once', 'there', 'large', 'caravan', 'going', 'through', 'desert']
data = f(*data, step=2, register=4, to_sort=True)
print(f(*data))

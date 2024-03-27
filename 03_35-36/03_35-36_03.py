def smart_search(*args, **ff):
    if isinstance(args[0], int):
        return search(*ff)
    elif all(isinstance(j, str) for j in args):
        return tuple(filter(lambda x: x[0].isupper(), args))


def search(ff):
    return ff % 2 == 0


print(smart_search('The', 'quick', 'brown', 'Fox', 'jumps', 'over', 'the', 'Lazy', 'Dog', func=lambda x: x))
print(smart_search(1, 2, 3, 5, 12, func=lambda x: x % 2))

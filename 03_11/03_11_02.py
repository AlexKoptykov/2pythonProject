def concatenate(*args: str) -> str:
    # print(args)
    lst = list(args)
    # print(lst)
    merge_lst = ''.join(lst)

    return merge_lst

first = "abc"
second = "def"
third = "gh"
print(concatenate(first, second, third))
print(concatenate(third, second, first))

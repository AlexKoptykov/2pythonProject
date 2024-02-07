def print_list(arg_list: list, sep: str) -> None:
    print(*arg_list, sep=sep)

arg_list = [4, "1a3", 4.3]
sep_line = "abc"

print_list(arg_list, sep_line)
print()
print_list(arg_list, "\n")

def sorted_names():
    names_list = [name for name in input().split(", ")]

    return sorted(names_list, key=lambda x: (-len(x), x))


print(sorted_names())
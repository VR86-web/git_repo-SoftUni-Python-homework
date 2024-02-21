n = int(input())


def printing(row, size):
    print(" " * (size - row), "* " * row)


def print_upper(size):
    for row in range(1, size + 1):
        printing(row, size)


def print_bottom(size):
    for row in range(size - 1, 0, - 1):
        printing(row, size)


def rhombus_of_stars(size):
    print_upper(size)
    print_bottom(size)


rhombus_of_stars(n)

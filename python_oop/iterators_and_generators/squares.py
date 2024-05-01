def squares(num):
    for n in range(1, num + 1):
        yield n ** 2


print(list(squares(5)))

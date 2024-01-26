def multiply(*numbers):
    result = 1
    for el in numbers:
        result *= el
    return result


print(multiply(1, 4, 5))


def func_executor(*data):
    result = []

    for funk_name, funk_numbers in data:
        result.append(f"{funk_name.__name__} - {funk_name(*funk_numbers)}")

    return "\n".join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)),(multiply_numbers, (2, 4))))
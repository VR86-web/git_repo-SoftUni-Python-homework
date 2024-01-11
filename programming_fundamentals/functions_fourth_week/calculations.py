def calculations(operation, a, b):
    if operation == "multiply":
        return a * b
    elif operation == "divide":
        return int(a / b)
    elif operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b


operation = input()
a = int(input())
b = int(input())
result = calculations(operation, a, b)
print(result)
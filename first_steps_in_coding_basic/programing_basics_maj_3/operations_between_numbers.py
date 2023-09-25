num_1 = int(input())
num_2 = int(input())
operator = input()
result = 0

if operator == "+" or operator == "-" or operator == "*":
    odd_or_even = ""
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    if result % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{num_1} {operator} {num_2} = {result} - {odd_or_even}")
elif operator == "/":
    if num_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        result = num_1 / num_2
        print(f"{num_1} / {num_2} = {result:.2f}")
elif operator == "%":
    if num_2 == 0:
        print(f"Cannot divide {num_1} by zero")
    else:
        result = num_1 % num_2
        print(f"{num_1} % {num_2} = {result}")



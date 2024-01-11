def factorial_numbers(number):
    for first_factorial in range(1, number):
        number *= first_factorial
    return number


first_number = int(input())
second_number = int(input())
first_number_factorial = factorial_numbers(first_number)
second_number_factorial = factorial_numbers(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")

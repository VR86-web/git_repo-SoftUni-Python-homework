def positive_numbers(numbers):
    return ", ".join(current_positive for current_positive in numbers if int(current_positive) >= 0)


def negative_numbers(numbers):
    return ", ". join(current_negative for current_negative in numbers if int(current_negative) < 0)


def even_numbers(numbers):
    return ", ".join(current_even for current_even in numbers if int(current_even) % 2 == 0)


def odd_numbers(numbers):
    return ", ".join(current_odd for current_odd in numbers if int(current_odd) % 2 != 0)


number = input().split(", ")
print(f"Positive: {positive_numbers(number)}")
print(f"Negative: {negative_numbers(number)}")
print(f"Even: {even_numbers(number)}")
print(f"Odd: {odd_numbers(number)}")

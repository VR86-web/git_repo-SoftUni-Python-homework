n = int(input())
number_is_special = True
for numbers in range(1, n + 1):
    current_number = str(numbers)
    digit_sum = 0
    for digit in current_number:
        digit_sum += int(digit)
    number_is_special = False
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        number_is_special = True
    print(f"{numbers} -> {number_is_special}")


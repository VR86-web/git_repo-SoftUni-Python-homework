def odd_and_even_sum(number: str):
    odd_counter = 0
    even_counter = 0
    for digits in number:
        if int(digits) % 2 == 0:
            even_counter += int(digits)
        else:
            odd_counter += int(digits)
    return odd_counter, even_counter


current_number = input()
sum_of_odd_digits, sum_of_even_digits = odd_and_even_sum(current_number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
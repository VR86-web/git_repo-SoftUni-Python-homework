def smallest(sum_numbers: list):
    return min(sum_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_element = smallest([first_number, second_number, third_number])
print(smallest_element)
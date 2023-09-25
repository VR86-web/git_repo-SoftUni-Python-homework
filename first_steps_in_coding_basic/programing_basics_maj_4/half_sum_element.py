import sys

count_of_numbers = int(input())
sum_of_all_elements = 0
max_element = -sys.maxsize
for number in range(count_of_numbers):
    current_element = int(input())
    sum_of_all_elements += current_element
    if current_element > max_element:
        max_element = current_element
if max_element == sum_of_all_elements - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    difference = abs(max_element - sum_of_all_elements + max_element)
    print("No")
    print(f"Diff = {difference}")



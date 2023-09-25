number = int(input())
total_sum_numbers = 0

while True:
    current_number = int(input())
    total_sum_numbers += current_number
    if total_sum_numbers >= number:
        print(total_sum_numbers)
        break

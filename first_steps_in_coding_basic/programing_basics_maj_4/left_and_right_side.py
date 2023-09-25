number = int(input())
first_sum = 0
second_sum = 0
for i in range(number):
    current_number_1 = int(input())
    first_sum += current_number_1

for i in range(number):
    current_number_2 = int(input())
    second_sum += current_number_2


if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    difference = abs(first_sum - second_sum)
    print(f"No, diff = {difference}")

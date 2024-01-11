n = int(input())
number = []
for num in range(n):
    current_number = int(input())
    number.append(current_number)
command = input()
filtered_numbers = []
if command == "even":
    for nums in number:
        if nums % 2 == 0:
            filtered_numbers.append(nums)
elif command == "odd":
    for nums in number:
        if nums % 2 != 0:
            filtered_numbers.append(nums)
elif command == "negative":
    for nums in number:
        if nums < 0:
            filtered_numbers.append(nums)
elif command == "positive":
    for nums in number:
        if nums >= 0:
            filtered_numbers.append(nums)
print(filtered_numbers)




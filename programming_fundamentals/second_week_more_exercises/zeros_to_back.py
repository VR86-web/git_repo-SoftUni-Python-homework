numbers = input().split(",")
numbers_list = []

for number in numbers:
    numbers_list.append(int(number))
number_of_zeros = numbers_list.count(0)
for zeros in numbers_list:
    numbers_list.remove(0)
    numbers_list.append(number_of_zeros * 0)
print(numbers_list)
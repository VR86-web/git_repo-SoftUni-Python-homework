text = input()
result = ""
numbers_list = [str(number) for number in text if number.isdigit()]
non_number_list = [char for char in text if not char.isdigit()]

for index, number in enumerate(numbers_list):
    if index % 2 == 0:
        result += "".join(non_number_list[:int(number)])
    non_number_list = non_number_list[int(number):]
print(result)

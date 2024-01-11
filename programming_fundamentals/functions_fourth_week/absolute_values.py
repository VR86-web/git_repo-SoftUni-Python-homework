number_list = input().split()
absolute_value = []
for numbers in number_list:
    absolute_value.append(abs(float(numbers)))
print(absolute_value)

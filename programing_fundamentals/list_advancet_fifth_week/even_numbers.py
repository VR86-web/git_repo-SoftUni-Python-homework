number_list = input().split(", ")
#number_list_as_int = [index for index, element in enumerate(number_list) if int(element) % 2 == 0]
#print(str(number_list_as_int))

result = []
for number in number_list:
    if int(number) % 2 == 0:
        result.append(number_list.index(number))
print(str(result))

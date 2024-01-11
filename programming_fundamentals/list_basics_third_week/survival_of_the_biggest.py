number_as_string = input().split()
numbers_to_remove = int(input())
number_as_int = []
for number in number_as_string:
    number_as_int.append(int(number))
for num in range(numbers_to_remove):
    number_as_int.remove(min(number_as_int))
print(*number_as_int, sep=", ")
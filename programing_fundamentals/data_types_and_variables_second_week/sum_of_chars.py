number_of_sums = int(input())
sum_counter = 0
for number in range(number_of_sums):
    letters = input()
    sum_counter += ord(letters)
print(f"The sum equals: {sum_counter}")
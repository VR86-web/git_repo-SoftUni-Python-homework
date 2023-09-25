from sys import maxsize

min_number = maxsize

while True:
    number = input()

    if number == "Stop":
        break
    current_number = int(number)
    if current_number < min_number:
        min_number = current_number
print(min_number)

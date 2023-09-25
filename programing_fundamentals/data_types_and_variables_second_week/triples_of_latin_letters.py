number = int(input())

for first_number in range(1, number + 1):
    for second_number in range(1, number + 1):
        for third_number in range(1, number + 1):
            print(f"{chr(96 + first_number)}{chr(96 + second_number)}{chr(96 + third_number)}")
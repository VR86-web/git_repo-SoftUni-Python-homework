number = int(input())
counter = 0
reached_number = False
for a in range(1, 9 + 1):
    for b in range(9, a, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c, -1):
                number_sum = a + b + c + d
                number_multiplication = a * b * c * d
                if number_sum == number_multiplication and number % 10 == 5:
                    counter += 1
                    print(f"{a}{b}{c}{d}")
                    reached_number = True
                    break
                elif number_multiplication // number_sum == 3 and number % 3 == 0:
                    counter += 1
                    print(f"{d}{c}{b}{a}")
                    reached_number = True
                    break
            if reached_number:
                break
        if reached_number:
            break
    if reached_number:
        break
if counter == 0:
    print("Nothing found")
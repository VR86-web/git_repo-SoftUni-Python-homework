available_sum = 0

while True:
    command = input()

    if command == "NoMoreMoney":
        break

    current_sum = float(command)

    if current_sum >= 0:
        available_sum += current_sum
        print(f"Increase: {current_sum:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {available_sum:.2f} ")





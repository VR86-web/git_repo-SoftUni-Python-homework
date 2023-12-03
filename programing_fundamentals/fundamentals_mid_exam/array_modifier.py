array_values = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "end":
        print(", ".join(map(str, array_values)))
        break
    if command[0] == "swap":
        array_values[int(command[1])], array_values[int(command[2])] \
            = array_values[int(command[2])], array_values[int(command[1])]
    elif command[0] == "multiply":
        array_values[int(command[1])] *= array_values[int(command[2])]
    elif command[0] == "decrease":
        array_values = [element - 1 for element in array_values]

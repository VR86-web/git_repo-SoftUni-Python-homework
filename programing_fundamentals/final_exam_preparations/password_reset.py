string = input()
new_password = ""
while True:
    command = input()
    if command == "Done":
        break
    tokens = command.split()
    action = tokens[0]
    if action == "TakeOdd":
        for letter in range(len(string)):
            if letter % 2 != 0:
                new_password += string[letter]
        print(new_password)
    elif action == "Cut":
        index, length = int(tokens[1]), int(tokens[2])
        new_password = new_password[0:index] + new_password[index + length::]
        print(new_password)
    elif action == "Substitute":
        substring, substitute = tokens[1], tokens[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {new_password}")
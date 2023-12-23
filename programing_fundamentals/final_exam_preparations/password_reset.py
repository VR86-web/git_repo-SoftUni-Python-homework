encrypted_password = input()
command = input()
while command != "Done":
    tokens = command.split()
    action = tokens[0]
    if action == "TakeOdd":
        new_password = ""
        for letter_index in range(1, len(encrypted_password), 2):
            new_password += encrypted_password[letter_index]
        encrypted_password = new_password
        print(encrypted_password)
    elif action == "Cut":
        index, length = int(tokens[1]), int(tokens[2])
        encrypted_password = encrypted_password[:index] + encrypted_password[index + length:]
        print(encrypted_password)
    elif action == "Substitute":
        substring, substitute = tokens[1], tokens[2]
        if substring in encrypted_password:
            encrypted_password = encrypted_password.replace(substring, substitute)
            print(encrypted_password)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {encrypted_password}")
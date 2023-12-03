def decoded_message(message, commands):
    for command in commands:
        tokens = command.split("|")
        instruction = tokens[0]

        if instruction == "Move":
            num_letters = int(tokens[1])
            message = message[num_letters:] + message[:num_letters]

        elif instruction == "Insert":
            index = int(tokens[1])
            value = tokens[2]
            message = message[:index] + value + message[index:]

        elif instruction == "ChangeAll":
            substring = tokens[1]
            replacement = tokens[2]
            message = message.replace(substring, replacement)

        elif instruction == "Decode":
            print(f"The decrypted message is: {message}")


encrypted_message = input()
command_list = []
while True:
    command = input()
    if command == "Decode":
        break

    command_list.append(command)


decoded_message(encrypted_message, command_list)

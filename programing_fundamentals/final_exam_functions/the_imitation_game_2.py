encrypted_message = input()


def move(message, letters):
    message = message[letters:] + message[:letters]
    return message


def insert(message, current_index, current_value):
    message = message[:current_index] + current_value + message[current_index:]
    return message


def change_all(message, current_substring, current_replacement):
    message = message.replace(current_substring, current_replacement)
    return message


while True:
    command = input()
    if command == "Decode":
        break
    tokens = command.split("|")
    instruction = tokens[0]

    if instruction == "Move":
        num_letters = int(tokens[1])
        encrypted_message = move(encrypted_message, num_letters)

    elif instruction == "Insert":
        index = int(tokens[1])
        value = tokens[2]
        encrypted_message = insert(encrypted_message, index, value)

    elif instruction == "ChangeAll":
        substring = tokens[1]
        replacement = tokens[2]
        encrypted_message = change_all(encrypted_message, substring, replacement)


print(f"The decrypted message is: {encrypted_message}")



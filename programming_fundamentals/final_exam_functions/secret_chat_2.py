def insert_space(message, current_index):
    message = message[:current_index] + " " + message[current_index:]
    print(message)
    return message


def reverse(message, current_substring):
    if current_substring in message:
        reversed_substring = current_substring[::-1]
        message = message.replace(current_substring, "")
        message = message + reversed_substring
        print(message)
        return message
    else:
        print("error")
        return message


def change_all(message, current_substring, current_replacement):
    message = message.replace(current_substring, current_replacement)
    print(message)
    return message


concealed_message = input()
command = input()
while command != "Reveal":
    tokens = command.split(":|:")
    action = tokens[0]
    if action == "InsertSpace":
        index = int(tokens[1])
        concealed_message = insert_space(concealed_message, index)

    elif action == "Reverse":
        substring = tokens[1]
        concealed_message = reverse(concealed_message, substring)

    elif action == "ChangeAll":
        substring, replacement = tokens[1], tokens[2]
        concealed_message = change_all(concealed_message, substring, replacement)

    command = input()

print(f"You have a new text message: {concealed_message}")
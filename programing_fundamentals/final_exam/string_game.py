string = input()

while True:
    command = input()
    if command == "Done":
        break
    tokens = command.split()
    action = tokens[0]
    if action == "Change":
        current_char, replacement = tokens[1], tokens[2]
        string = string.replace(current_char, replacement)
        print(string)

    elif action == "Includes":
        substring = tokens[1]
        if substring in string:
            print(f"True")
        else:
            print(f"False")

    elif action == "End":
        substring = tokens[1]
        result = string.endswith(substring)
        print(result)

    elif action == "Uppercase":
        print(string.upper())

    elif action == "FindIndex":
        char = tokens[1]
        index = string.find(char)
        print(index)

    elif action == "Cut":
        start_index, count = int(tokens[1]), int(tokens[2])
        string = string[start_index: start_index + count]
        print(string)
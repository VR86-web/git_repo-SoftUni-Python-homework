activation_key = input()

command = input()
while command != "Generate":
    tokens = command.split(">>>")
    if tokens[0] == "Contains":
        substring = tokens[1]
        if substring in activation_key:
            print(f"{activation_key}contains {substring}")
        else:
            print(f"Substring not found!")

    elif tokens[0] == "Flip":
        case_sensitive = tokens[1]
        start_index = int(tokens[2])
        end_index = int(tokens[3])
        if case_sensitive == "Upper":
            new_part = activation_key[start_index:end_index].upper()
            activation_key = activation_key.replace(activation_key[start_index:end_index], new_part)
            print(activation_key)
        elif case_sensitive == "Lower":
            new_part = activation_key[start_index:end_index].lower()
            activation_key = activation_key.replace(activation_key[start_index:end_index], new_part)
            print(activation_key)

    elif tokens[0] == "Slice":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        activation_key = activation_key.replace(activation_key[start_index:end_index], "")
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")

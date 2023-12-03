def data_types(command: str, number_or_string):
    if command == "int":
        result = int(number_or_string) * 2
        return result
    elif command == "real":
        result = float(number_or_string) * 1.5
        return f"{result:.2f}"
    elif command == "string":
        result = f"${number_or_string}$"
        return result


current_command = input()
current_number_ot_str = input()
print(data_types(current_command, current_number_ot_str))




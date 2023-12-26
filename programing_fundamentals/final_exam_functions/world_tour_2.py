stops = input()


def add_stop(data, current_index, current_string):
    if 0 < current_index < len(data):
        data = data[0:current_index] + current_string + data[current_index:]
        return data


def remove_stop(data, current_start_index, current_end_index):
    if 0 < current_start_index < len(data) and 0 < current_end_index < len(data):
        data = data[0:current_start_index] + data[current_end_index + 1:]
        return data


def switch(data, current_old_string, current_new_string):
    if current_old_string in data:
        data = data.replace(current_old_string, current_new_string)
        return data
    else:
        return data


command = input()
while command != "Travel":
    tokens = command.split(":")
    action = tokens[0]
    if action == "Add Stop":
        index = int(tokens[1])
        string = tokens[2]
        stops = add_stop(stops, index, string)
        print(stops)

    elif action == "Remove Stop":
        start_index = int(tokens[1])
        end_index = int(tokens[2])
        stops = remove_stop(stops, start_index, end_index)
        print(stops)

    elif action == "Switch":
        old_string = tokens[1]
        new_string = tokens[2]
        stops = switch(stops, old_string, new_string)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
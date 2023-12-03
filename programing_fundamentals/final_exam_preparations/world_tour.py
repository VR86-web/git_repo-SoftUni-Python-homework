stops = input()
command = input()
while command != "Travel":
    travel_info = command.split(":")
    if travel_info[0] == "Add Stop":
        index = int(travel_info[1])
        string = travel_info[2]
        if index in range(len(stops)):
            stops = stops[:index] + string + stops[index:]
    elif travel_info[0] == "Remove Stop":
        start_index = int(travel_info[1])
        end_index = int(travel_info[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index+1:]
    elif travel_info[0] == "Switch":
        old_string = travel_info[1]
        new_string = travel_info[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input()
print(f"Ready for world tour! Planned stops: {stops}")
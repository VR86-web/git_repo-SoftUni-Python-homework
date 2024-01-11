registered_users_dict = {}
number_of_commands = int(input())
for current_number in range(number_of_commands):
    data = input().split()
    if data[0] == "register":
        username = data[1]
        plate_number = data[2]
        if username in registered_users_dict:
            print(f"ERROR: already registered with plate number {registered_users_dict[username]}")
        else:
            registered_users_dict[username] = plate_number
            print(f"{username} registered {registered_users_dict[username]} successfully")
    elif data[0] == "unregister":
        username = data[1]
        if username not in registered_users_dict.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del registered_users_dict[username]
for username, plate_number in registered_users_dict.items():
    print(f"{username} => {plate_number}")

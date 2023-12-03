resources_count_dict = {}

while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    if command not in resources_count_dict.keys():
        resources_count_dict[command] = 0
    resources_count_dict[command] += quantity
for command, quantity in resources_count_dict.items():
    print(f"{command} -> {quantity}")
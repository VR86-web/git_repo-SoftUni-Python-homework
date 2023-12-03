number_of_plants = int(input())
plant_dict = {}
for number in range(number_of_plants):
    plant_info = input().split("<->")
    plant, rarity = plant_info[0], int(plant_info[1])
    plant_dict[plant] = {'rarity': rarity, 'rating': []}
while True:
    command = input()
    if command == "Exhibition":
        break
    command_args = command.split(": ")
    action = command_args[0]
    if action == "Rate":
        args = command_args[1].split(" - ")
        plant, rating = args[0], int(args[1])
        if plant not in plant_dict:
            print("error")
        else:
            plant_dict[plant]['rating'].append(rating)
    elif action == "Update":
        plant, new_rarity = command_args[1].split(" - ")
        if plant not in plant_dict:
            print("error")
        else:
            plant_dict[plant]['rarity'] = new_rarity
    elif action == "Reset":
        plant = command_args[1]
        if plant not in plant_dict:
            print("error")
        else:
            plant_dict[plant]['rating'].clear()
print("Plants for the exhibition:")
for plant, plant_information in plant_dict.items():
    if len(plant_information['rating']) > 0:
        average_rating = sum(plant_information['rating']) / len(plant_information['rating'])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {plant_information['rarity']}; Rating: {average_rating:.2f}")

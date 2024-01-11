
def rate(data, current_plant, current_rating):
    if current_plant in data:
        data[current_plant]["rating"].append(current_rating)
        return data
    else:
        print("error")
        return data


def update(data, current_plant, current_new_rarity):
    if current_plant in data:
        data[current_plant]["rarity"] = int(current_new_rarity)
        return data
    else:
        print("error")
        return data


def reset(data, current_plant):
    if current_plant in data:
        data[current_plant]["rating"].clear()
        return data
    else:
        print("error")
        return data


plants_info = int(input())
plant_dict = {}
for number in range(plants_info):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = int(plant_info[1])
    plant_dict[plant] = {"rarity": rarity, "rating": []}

while True:
    command = input()
    if command == "Exhibition":
        break
    tokens = command.split(": ")
    action = tokens[0]
    if action == "Rate":
        args = tokens[1].split(" - ")
        plant = args[0]
        rating = int(args[1])
        plant_dict = rate(plant_dict, plant, rating)

    elif action == "Update":
        args = tokens[1].split(" - ")
        plant = args[0]
        new_rarity = int(args[1])
        plant_dict = update(plant_dict, plant, new_rarity)

    elif action == "Reset":
        plant = tokens[1]
        plant_dict = reset(plant_dict, plant)

print("Plants for the exhibition:")
for key, value in plant_dict.items():
    if len(value["rating"]) > 0:
        average_rating = sum(value["rating"]) / len(value["rating"])
    else:
        average_rating = 0
    print(f"- {key}; Rarity: {value['rarity']}; Rating: {average_rating:.2f}")
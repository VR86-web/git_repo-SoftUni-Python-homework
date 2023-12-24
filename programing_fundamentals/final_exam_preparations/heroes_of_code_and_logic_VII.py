number_of_heroes = int(input())
heroes_dict = {}
for heroes in range(number_of_heroes):
    data = input().split()
    hero_name = data[0]
    hit_points = int(data[1])
    mana_points = int(data[2])
    if hero_name not in heroes_dict:
        heroes_dict[hero_name] = {"HP": hit_points, "MP": mana_points}

while True:
    command = input().split(" - ")
    action = command[0]
    if action == "End":
        break
    if action == "CastSpell":
        hero = command[1]
        mana_points_needed = int(command[2])
        spell_name = command[3]
        if heroes_dict[hero]["MP"] >= mana_points_needed:
            heroes_dict[hero]["MP"] -= mana_points_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes_dict[hero]['MP']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        hero = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes_dict[hero]["HP"] -= damage
        if heroes_dict[hero]["HP"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero]['HP']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes_dict[hero]

    elif action == "Recharge":
        hero = command[1]
        amount = int(command[2])
        heroes_dict[hero]["MP"] += amount
        if heroes_dict[hero]["MP"] > 200:
            print(f"{hero} recharged for {heroes_dict[hero]['MP'] - 200} MP!")
            heroes_dict[hero]["MP"] = 200
        else:
            print(f"{hero} recharged for {amount} MP!")

    elif action == "Heal":
        hero = command[1]
        amount = int(command[2])
        heroes_dict[hero]["HP"] += amount
        if heroes_dict[hero]["HP"] > 100:
            print(f"{hero} healed for {heroes_dict[hero]['HP'] - 100} HP!")
            heroes_dict[hero]["HP"] = 100
        else:
            print(f"{hero} healed for {amount} HP!")
for key, value in heroes_dict.items():
    print(key)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")
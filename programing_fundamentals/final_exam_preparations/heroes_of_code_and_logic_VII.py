number_of_heroes = int(input())
for heroes in range(number_of_heroes):
    data = input().split()
    hero_name = data[0]
    hit_points = int(data[1])
    mana_points = int(data[2])

while True:
    command = input().split(" - ")
    action = command[0]
    if action == "End":
        break
    if action == "CastSpell":
        hero_name = command[1]
        mana_points_needed = int(command[2])
        spell_name = command[3]
        
    elif action == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
    elif action == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
    elif action == "Heal":
        hero_name = command[1]
        amount = int(command[2])

initial_energy = int(input())
command = input()
won_battles_counter = 0
while command != "End of battle":
    distance_of_an_enemy = int(command)
    if initial_energy >= distance_of_an_enemy:
        initial_energy -= distance_of_an_enemy
        won_battles_counter += 1
        if won_battles_counter % 3 == 0:
            initial_energy += won_battles_counter
    else:
        print(f"Not enough energy! Game ends with {won_battles_counter} "
              f"won battles and {initial_energy} energy")
        break
    command = input()
    if command == "End of battle":
        print(f"Won battles: {won_battles_counter}. Energy left: {initial_energy}")
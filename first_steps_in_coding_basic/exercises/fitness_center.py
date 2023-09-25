number_of_clients_in_fitness = int(input())
back_training_counter = 0
chest_training_counter = 0
legs_training_counter = 0
abs_training_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0

for activity in range(number_of_clients_in_fitness):
    fitness_activity = input()
    if fitness_activity == "Back":
        back_training_counter += 1
    elif fitness_activity == "Chest":
        chest_training_counter += 1
    elif fitness_activity == "Legs":
        legs_training_counter += 1
    elif fitness_activity == "Abs":
        abs_training_counter += 1
    elif fitness_activity == "Protein shake":
        protein_shake_counter += 1
    elif fitness_activity == "Protein bar":
        protein_bar_counter += 1
total_number_training_people = back_training_counter + chest_training_counter \
                               + legs_training_counter + abs_training_counter
percentage_training_people = total_number_training_people * 100 / number_of_clients_in_fitness
total_number_of_protein_buyers = protein_bar_counter + protein_shake_counter
percentage_protein_buyers = total_number_of_protein_buyers * 100 / number_of_clients_in_fitness
print(f"{back_training_counter} - back")
print(f"{chest_training_counter} - chest")
print(f"{legs_training_counter} - legs")
print(f"{abs_training_counter} - abs")
print(f"{protein_shake_counter} - protein shake")
print(f"{protein_bar_counter} - protein bar")
print(f"{percentage_training_people:.2f}% - work out")
print(f"{percentage_protein_buyers:.2f}% - protein")

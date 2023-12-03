population = [int(people) for people in input().split(", ")]
minimum_wealth = int(input())
for current_number in range(len(population)):
    if population[current_number] < minimum_wealth:
        max_number = max(population)
        difference = minimum_wealth - population[current_number]
        if max_number - difference >= minimum_wealth:
            population[population.index(max_number)] -= difference
            population[current_number] += difference
if sum(population) >= len(population) * minimum_wealth:
    print(population)
else:
    print("No equal distribution possible")


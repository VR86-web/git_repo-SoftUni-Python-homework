number_of_electrons = int(input())
electrons_list = []
for shells in range(1, number_of_electrons + 1):
    shells_capacity = 2 * shells ** 2
    if number_of_electrons >= shells_capacity:
        electrons_list.append(shells_capacity)
        number_of_electrons -= shells_capacity
        if number_of_electrons == 0:
            break
    else:
        electrons_list.append(number_of_electrons)
        break
print(electrons_list)
number_of_lines = int(input())
tank_capacity = 255
litters_in_tank = 0
for litters in range(number_of_lines):
    litters_of_water = int(input())
    if tank_capacity - litters_of_water< 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litters_of_water
    litters_in_tank += litters_of_water
print(litters_in_tank)
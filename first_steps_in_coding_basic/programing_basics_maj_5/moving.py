width_of_free_space = int(input())
length_of_free_space = int(input())
height_of_free_space = int(input())
cubes_free_space = width_of_free_space * length_of_free_space * height_of_free_space
free_space_left = True
command = input()
while command != "Done":
    number_of_cubes = int(command)
    cubes_free_space -= number_of_cubes
    if cubes_free_space < 0:
        free_space_left = False
        break
    command = input()
if cubes_free_space >= 0:
    print(f"No more free space! You need {cubes_free_space} Cubic meters more.")
else:
    print(f"{abs(cubes_free_space)} Cubic meters left.")




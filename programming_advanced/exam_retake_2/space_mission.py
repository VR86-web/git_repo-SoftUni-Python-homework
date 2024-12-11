n = int(input())

matrix = []
spaceship_position = []
resources = 100

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "S":
            spaceship_position = [row, col]
            matrix[row][col] = "."

while True:
    command = input()

    new_row, new_col = spaceship_position[0] + directions[command][0], spaceship_position[1] + directions[command][1]

    if not (0 <= new_row < n and 0 <= new_col < n):
        print("Mission failed! The spaceship was lost in space.")
        break

    spaceship_position = [new_row, new_col]

    resources -= 5

    if matrix[new_row][new_col] == "M":
        resources -= 5
        matrix[new_row][new_col] = "."

    elif matrix[new_row][new_col] == "R":
        resources = min(resources + 10, 100)

    elif matrix[new_row][new_col] == "P":
        if resources >= 0:
            print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
        break

    if resources < 5:
        print("Mission failed! The spaceship was stranded in space.")
        matrix[new_row][new_col] = "S"
        break

if matrix[spaceship_position[0]][spaceship_position[1]] != "P":
    matrix[spaceship_position[0]][spaceship_position[1]] = "S"

for row in matrix:
    print(" ".join(row))




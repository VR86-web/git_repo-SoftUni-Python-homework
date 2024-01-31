size = int(input())

territory = []
snake_pos = []
lair_pos = []

food_quantity = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    territory.append(list(input()))

    if "S" in territory[row]:
        snake_pos = [row, territory[row].index("S")]
    if "B" in territory[row]:
        lair_pos.append((row, territory[row].index("B")))

while True:
    commands = input()

    next_row = snake_pos[0] + directions[commands][0]
    next_col = snake_pos[1] + directions[commands][1]
    territory[snake_pos[0]][snake_pos[1]] = "."

    if not (0 <= next_row < size and 0 <= next_col < size):
        print("Game over!")
        break

    element = territory[next_row][next_col]

    if element == "*":
        food_quantity += 1
        snake_pos = [next_row, next_col]

    elif element == "B":
        territory[next_row][next_col] = "."
        lair_pos.remove((next_row, next_col))
        snake_pos = lair_pos[0]

    else:
        snake_pos = [next_row, next_col]

    territory[snake_pos[0]][snake_pos[1]] = "S"

    if food_quantity == 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food_quantity}")

[print("".join(row)) for row in territory]




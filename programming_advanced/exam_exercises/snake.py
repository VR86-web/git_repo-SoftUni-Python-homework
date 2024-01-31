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
    territory.append(input())

    if "S" in territory[row]:
        snake_pos = [row, territory[row].index("S")]
    if "B" in territory[row]:
        lair_pos.append((row, territory[row].index("B")))

while food_quantity < 10:
    commands = input()

    row = snake_pos[0] + directions[commands][0]
    col = snake_pos[1] + directions[commands][1]

    if not (0 <= row < size and 0 <= col < size):
        print("Game over!")
        break

    element = territory[row][col]

    if element == "*":
        snake_pos = [row, col]
        food_quantity += 1

    elif element == "B":
        lair_pos.remove((row, col))
        snake_pos = lair_pos[0]


if food_quantity == 10:
    print("You won! You fed the snake.")

print(f"Food eaten: {food_quantity}")

[print("".join(row)) for row in territory]




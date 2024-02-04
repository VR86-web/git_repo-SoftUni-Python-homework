size = int(input())

player_row, player_col = 0, 0

total_coins = 0
field = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    current_row = input().split()
    field.append(current_row)

    if "P" in current_row:
        player_row, player_col = row, current_row.index("P")

path = [[player_row, player_col]]
winner = False

while not winner:
    command = input()
    if command not in ["up", "down", "left", "right"]:
        continue

    field[player_row][player_col] = 0
    player_row += directions[command][0]
    player_col += directions[command][1]

    if player_row < 0:
        player_row = size - 1
    elif player_row == size:
        player_row = 0

    if player_col < 0:
        player_col = size - 1
    elif player_col == size:
        player_col = 0

    element = field[player_row][player_col]
    path.append([player_row, player_col])

    if element == "X":
        total_coins = int(total_coins/2)
        break

    elif str(element).isdigit():
        total_coins += int(element)

    field[player_row][player_col] = 0

    if total_coins >= 100:
        winner = True
        print(f"You won! You've collected {total_coins} coins.")
        break

if not winner:
    print(f"Game over! You've collected {total_coins} coins.")

print("Your path:")
[print(el) for el in path]

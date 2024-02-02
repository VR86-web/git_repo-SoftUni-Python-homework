word = input()
size = int(input())

matrix = []
player_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append(list(input()))

    if "P" in matrix[row]:
        player_pos = [row, matrix[row].index("P")]

number = int(input())
for _ in range(number):
    command = input()
    new_row = player_pos[0] + directions[command][0]
    new_col = player_pos[1] + directions[command][1]

    if new_row not in range(size) or new_col not in range(size):
        word = word[:-1]
        continue

    matrix[player_pos[0]][player_pos[1]] = "-"
    player_pos = [new_row, new_col]
    element = matrix[player_pos[0]][player_pos[1]]

    if element != "-":
        word += element

    matrix[player_pos[0]][player_pos[1]] = "P"

print(word)

[print("".join(x))for x in matrix]

size = int(input())

airspace = []

jet_pos = []

armour_value = 300
enemies_counter = 4

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for row in range(size):
    current_row = list(input())
    airspace.append(current_row)

    if 'J' in current_row:
        jet_pos = [row, current_row.index("J")]
        airspace[row][current_row.index("J")] = "-"

row, col = jet_pos

while enemies_counter > 0:
    commands = input()
    row += direction_mapper[commands][0]
    col += direction_mapper[commands][1]

    if airspace[row][col] == "E":
        airspace[row][col] = "-"
        enemies_counter -= 1
        if enemies_counter == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        else:
            armour_value -= 100
            if armour_value == 0:
                print(f"Mission failed, your jetfighter was shot down!"
                    f" Last coordinates [{row}, {col}]!")
                break

    elif airspace[row][col] == "R":
        armour_value = min(300, armour_value + 100)
        airspace[row][col] = "-"

airspace[row][col] = "J"

[print(*row, sep="") for row in airspace]


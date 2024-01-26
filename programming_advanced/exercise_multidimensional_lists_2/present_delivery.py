def eat_cookie(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_position[0] + coordinates[0]
        c = santa_position[1] + coordinates[1]

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == "V":
                nice_kids += 1

            neighborhood[r][c] = "-"
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


number_of_presents = int(input())
size = int(input())

neighborhood = []
santa_position = []

total_nice_kids = 0
nice_kids_visited = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    neighborhood.append(input().split())

    if "S" in neighborhood[row]:
        santa_position = [row, neighborhood[row].index("S")]
        neighborhood[row][santa_position[1]] = "-"

    total_nice_kids += neighborhood[row].count("V")

command = input()

while command != "Christmas morning":
    santa_position = [
        santa_position[0] + directions[command][0],
        santa_position[1] + directions[command][1]
    ]

    house = neighborhood[santa_position[0]][santa_position[1]]

    if house == "V":
        number_of_presents -= 1
        nice_kids_visited += 1
    elif house == "C":
        number_of_presents, nice_kids_visited = eat_cookie(number_of_presents, nice_kids_visited)

    neighborhood[santa_position[0]][santa_position[1]] = "-"

    if not number_of_presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

neighborhood[santa_position[0]][santa_position[1]] = "S"

if not number_of_presents and nice_kids_visited < total_nice_kids:
    print("Santa ran out of presents!")

[print(*row)for row in neighborhood]

if nice_kids_visited == total_nice_kids:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")
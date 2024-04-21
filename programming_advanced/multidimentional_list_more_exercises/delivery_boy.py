def is_in_scoop(row, col, row_count, col_count):
    return 0 <= row < row_count and 0 <= col < col_count


n, m = [int(el) for el in input().split()]

neighborhood = []
current_pos = None
delivery_boy_pos = None

directions = {
    "up": (- 1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1)
}

for row_index in range(n):
    data = list(input())

    if "B" in data:
        col_index = data.index("B")
        delivery_boy_pos = (row_index, col_index)
    neighborhood.append(data)

current_pos = delivery_boy_pos
while True:
    command = input()
    next_row, next_col = current_pos[0] + directions[command][0], current_pos[1] + directions[command][1]

    if not is_in_scoop(next_row, next_col, n, m):
        neighborhood[delivery_boy_pos[0]][delivery_boy_pos[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    symbol = neighborhood[next_row][next_col]

    if symbol == "*":
        continue

    current_pos = [next_row, next_col]

    if symbol == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        neighborhood[next_row][next_col] = "R"

    elif symbol == "A":
        print("Pizza is delivered on time! Next order...")
        neighborhood[next_row][next_col] = "P"

        break

    elif symbol == "-":
        neighborhood[next_row][next_col] = "."

for row in neighborhood:
    print("".join(row))

size = int(input())

matrix = []
bunny_pos = []
best_path_pos = []
max_collected_eggs = float("-inf")
best_way = None

directions = {
    "up": (- 1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1)
}

for row in range(size):
    matrix.append((input().split()))

    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index("B")]

for direction, positions in directions.items():
    row, col = [bunny_pos[0] + positions[0], bunny_pos[1] + positions[1]]

    path = []
    collected_eggs = 0

    while 0 <= row < size and 0 <= col < size:

        if matrix[row][col] == "X":
            break
        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_path_pos = path
        best_way = direction

print(best_way)
print(*best_path_pos, sep="\n")
print(max_collected_eggs)


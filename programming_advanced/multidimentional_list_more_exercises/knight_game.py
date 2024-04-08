size = int(input())
matrix = [list(input()) for _ in range(size)]

positions = {
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
}

removed_knights = 0

while True:
    knight_with_most_attacks_pos = []
    max_knight_attacked = 0

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for position in positions:
                    new_row = row + position[0]
                    new_col = col + position[1]

                    if 0 <= new_row < size and 0 <= new_col < size:
                        if matrix[new_row][new_col] == "K":
                            attacks += 1

                if attacks > max_knight_attacked:
                    max_knight_attacked = attacks
                    knight_with_most_attacks_pos = [row, col]

    if knight_with_most_attacks_pos:
        r, c = knight_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_knights += 1

    else:
        break

print(removed_knights)

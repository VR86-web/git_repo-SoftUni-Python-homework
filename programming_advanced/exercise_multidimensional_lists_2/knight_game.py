n = int(input())

matrix = [list(input()) for _ in range(n)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, -1),
    (2, 1),
    (1, -2),
    (1, 2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attack_pos = []

    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "K":
                attacks = 0

                for position in positions:
                    pos_row = row + position[0]
                    pos_col = col + position[1]

                    if 0 <= pos_row < n and 0 <= pos_col < n:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_with_most_attack_pos = [row, col]

    if knight_with_most_attack_pos:
        r, c = knight_with_most_attack_pos
        matrix[r][c] = "0"
        removed_knights += 1

    else:
        break

print(removed_knights)




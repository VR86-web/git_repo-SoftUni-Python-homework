n = int(input())
field = [list(input()) for _ in range(n)]

stars = 2
row, col = next((i, j) for i in range(n) for j in range(n) if field[i][j] == 'P')

moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
while stars > 0 and stars < 10:
    direction = input()
    dr, dc = moves[direction]
    new_row, new_col = row + dr, col + dc

    if 0 <= new_row < n and 0 <= new_col < n:
        if field[new_row][new_col] == '*':
            stars += 1
        elif field[new_row][new_col] == '#':
            stars -= 1
        field[row][col], field[new_row][new_col] = '.', 'P'
        row, col = new_row, new_col
    else:
        pass  # Handle out-of-bounds

print("You won! You have collected 10 stars." if stars >= 10 else "Game over! You are out of any stars.")
print(f"Your final position is [{row}, {col}]")
for row in field:
    print(*row)
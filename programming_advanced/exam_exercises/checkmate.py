SIZE = 8
chessboard = []
queens_pos = []
queens_win = []

directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, 1],
    [1, 1],
    [1, -1],
    [-1, -1]
]

for row in range(SIZE):
    new_row = input().split()
    chessboard.append(new_row)
    for col in range(len(new_row)):
        if chessboard[row][col] == "Q":
            queens_pos.append([row, col])

for queen in queens_pos:
    row, col = queen[0], queen[1]
    for direction in directions:
        check_pos = [row, col]
        while check_pos[0] in range(SIZE) and check_pos[1] in range(SIZE):
            new_row = check_pos[0] + direction[0]
            new_col = check_pos[1] + direction[1]
            if new_row in range(SIZE) and new_col in range(SIZE):
                if chessboard[new_row][new_col] == "Q":
                    break
                if chessboard[new_row][new_col] == "K":
                    queens_win.append(queen)
                    break
            check_pos = [new_row, new_col]

if queens_win:
    for position in queens_win:
        print(position)
else:
    print(f'The king is safe!')
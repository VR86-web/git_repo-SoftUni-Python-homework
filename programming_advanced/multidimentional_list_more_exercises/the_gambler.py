size = int(input())

matrix = []
gambling_pos = []

initial_entering_amount = 100

directions = {
    "up": (- 1, 0),
    "down": (1, 0),
    "left": (0, - 1),
    "right": (0, 1)
}

for row_index in range(size):
    data = list(input())
    if "G" in data:
        col_index = data.index("G")
        gambling_pos = [row_index, col_index]
    matrix.append(data)

command = input()

while command != 'end':
    row = gambling_pos[0] + directions[command][0]
    col = gambling_pos[1] + directions[command][1]

    if not (0 <= row < size and 0 <= col < size):
        print("Game over! You lost everything!")
        exit()

    matrix[gambling_pos[0]][gambling_pos[1]] = "-"
    gambling_pos = [row, col]
    element = matrix[row][col]
    matrix[row][col] = "G"

    command = input()

    if element == "W":
        initial_entering_amount += 100

    elif element == "P":
        initial_entering_amount -= 200
        if initial_entering_amount <= 0:
            print("Game over! You lost everything!")
            exit()
    elif element == "J":
        initial_entering_amount += 100000
        print("You win the Jackpot!")
        break

print(f"End of the game. Total amount: {initial_entering_amount}$")
[print("".join(el))for el in matrix]

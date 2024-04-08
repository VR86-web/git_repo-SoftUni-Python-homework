size = int(input())

matrix = [[int(r) for r in input().split()] for _ in range(size)]

command = input().split()

while command[0] != "END":

    command_type, r, c, number = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= r < size and 0 <= c < size):
        print("Invalid coordinates")

    elif command_type == "Add":
        matrix[r][c] += number

    elif command_type == "Subtract":
        matrix[r][c] -= number

    command = input().split()

[print(*r) for r in matrix]


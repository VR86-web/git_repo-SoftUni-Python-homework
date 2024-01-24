n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

command = input().split()

while command[0] != "END":
    type_command, r, c, number = command[0], int(command[1]), int(command[2]), int(command[3])
    if not (0 <= r < n and 0 <= c < n):
        print("Invalid coordinates")
    elif type_command == "Add":
        matrix[r][c] += number
    elif type_command == "Subtract":
        matrix[r][c] -= number

    command = input().split()

[print(*row) for row in matrix]
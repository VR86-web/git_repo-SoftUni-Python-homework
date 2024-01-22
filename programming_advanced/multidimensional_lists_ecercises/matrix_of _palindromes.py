rows, cols = [int(x) for x in input().split()]

start_index = ord("a")
matrix = []

for row in range(start_index, start_index + rows):
    for col in range(row, row + cols):
        print(chr(row), chr(col), chr(row), sep="", end=" ")

    print()

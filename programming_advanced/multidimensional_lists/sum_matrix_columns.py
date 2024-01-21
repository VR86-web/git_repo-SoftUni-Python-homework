rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    num_data = [int(x) for x in input().split()]
    matrix.append(num_data)

for col_index in range(cols):
    cols_sum = 0
    for row_index in range(rows):
        cols_sum += matrix[row_index][col_index]
    print(cols_sum)

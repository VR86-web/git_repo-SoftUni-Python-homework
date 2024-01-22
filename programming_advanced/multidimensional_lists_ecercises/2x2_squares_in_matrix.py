rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for _ in range(rows)]

equal_matrices_sum = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        current_index = matrix[row][col]

        if current_index == matrix[row][col+1]\
                and current_index == matrix[row+1][col]\
                and current_index == matrix[row+1][col+1]:
            equal_matrices_sum += 1

print(equal_matrices_sum)




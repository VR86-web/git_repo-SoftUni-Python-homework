rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

max_sum = float("-inf")
sub_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        first_line = matrix[row][col:col+3]
        second_line = matrix[row+1][col:col+3]
        third_line = matrix[row+2][col:col+3]

        total_sum = sum(first_line) + sum(second_line) + sum(third_line)

        if total_sum > max_sum:
            max_sum = total_sum
            sub_matrix = [first_line, second_line, third_line]

print(f"Sum = {max_sum}")
[print(*row) for row in sub_matrix]



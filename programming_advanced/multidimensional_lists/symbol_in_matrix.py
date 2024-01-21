number = int(input())

matrix = []

for _ in range(number):
    matrix.append(list(input()))

searched_element = input()

for row_index in range(number):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_element:
            print(f"({row_index}, {col_index})")
            exit()

else:
    print(f"{searched_element} does not occur in the matrix")
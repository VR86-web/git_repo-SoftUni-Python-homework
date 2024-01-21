rows = int(input())

flatten_matrix = []

for i in range(rows):
    nums_data = [int(x) for x in input().split(", ")]
    flatten_matrix.extend(nums_data)

print(flatten_matrix)

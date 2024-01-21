rows, cols = [int(x) for x in input().split(", ")]
total_amount = 0

matrix = []
for i in range(rows):
    nums = [int(x) for x in input().split(", ")]
    total_amount += sum(nums)
    matrix.append(nums)

print(total_amount)
print(matrix)

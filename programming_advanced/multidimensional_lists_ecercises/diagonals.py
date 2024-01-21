num = int(input())

matrix = [[int(x) for x in input().split(", ")]for _ in range(num)]

primary = [matrix[row][row] for row in range(num)]
secondary = [matrix[row][num - row - 1] for row in range(num)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")

n = int(input())
p1_counter = 0
p2_counter = 0
p3_counter = 0

for number in range(n):
    numbers = int(input())
    if numbers % 2 == 0:
        p1_counter += 1
    if numbers % 3 == 0:
        p2_counter += 1
    if numbers % 4 == 0:
        p3_counter += 1
print(f'{p1_counter / n * 100:.2f}%')
print(f'{p2_counter / n * 100:.2f}%')
print(f'{p3_counter / n * 100:.2f}%')
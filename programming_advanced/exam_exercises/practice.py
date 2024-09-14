n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    line = input()
    if line == 'END':
        break

    command = line.split()
    row, col, value = [int(x) for x in command[1:3]]
    if 0 <= row < n and 0 <= col < n:
        print(f'Invalid coordinates')
        continue
    
size = int(input())

territory = []
alice_pos = []

bags_tea = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    territory.append(input().split())

    if "A" in territory[row]:
        alice_pos = [row, territory[row].index("A")]
        territory[row][alice_pos[1]] = "*"

while bags_tea < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    element = territory[row][col]
    territory[row][col] = "*"

    if element == "R":
        break

    if element.isdigit():
        bags_tea += int(element)

if bags_tea >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in territory]



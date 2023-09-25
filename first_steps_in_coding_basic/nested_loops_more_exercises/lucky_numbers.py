number = int(input())
for x in range(1, 9 + 1):
    for y in range(1, 9 + 1):
        for z in range(1, 9 + 1):
            for k in range(1, 9 + 1):
                if x + y == z + k:
                    if number % (x + y) == 0:
                        print(f"{x}{y}{z}{k}", end=" ")








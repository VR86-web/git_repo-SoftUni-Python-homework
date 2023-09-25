first_number = int(input())
second_number = int(input())
for x in range(first_number, second_number + 1):
    for y in range(first_number, second_number + 1):
        for z in range(first_number, second_number + 1):
            for k in range(first_number, second_number + 1):
                if x % 2 == 0 and k % 2 != 0:
                    if x > k:
                        if (y + z) % 2 == 0:
                            print(f"{x}{y}{z}{k}", end=" ")
                            continue
                elif x % 2 != 0 and k % 2 == 0:
                    if x > k:
                        if (y + z) % 2 == 0:
                            print(f"{x}{y}{z}{k}", end=" ")





max_num1 = int(input())
max_num2 = int(input())
max_num3 = int(input())
for n1 in range(2, max_num1 + 1, 2):
    for n2 in range(2, max_num2 + 1):
        for n3 in range(2, max_num3 + 1, 2):
            if n2 == 2 or n2 == 3 or n2 == 5 or n2 == 7:
                print(f"{n1} {n2} {n3}")
n = int(input())
for j in range(n):
    for k in range(j + 1):
        print("*", end="")
    print()
for j in range(n):
    for k in range(n - j - 1):
        print("*", end="")
    print()
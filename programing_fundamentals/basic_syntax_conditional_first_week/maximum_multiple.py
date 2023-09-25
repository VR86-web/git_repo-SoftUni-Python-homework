divisor = int(input())
boundary = int(input())
for numbers in range(boundary, divisor - 1, -1):
    if numbers % divisor == 0:
        break
print(numbers)
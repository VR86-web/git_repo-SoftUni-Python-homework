from collections import deque


def zero_case(gender):
    if gender <= 0:
        return True


def value_divisible(gender):
    if gender % 25 == 0:
        return True


males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

matches = 0

while males and females:
    male = males.pop()

    if zero_case(male):
        continue

    if value_divisible(male):
        males.pop()
        continue

    female = females.popleft()
    if zero_case(female):
        males.append(male)
        continue

    if value_divisible(female):
        females.popleft()
        males.append(male)
        continue

    if male == female:
        matches += 1
    else:
        males.append(male - 2)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
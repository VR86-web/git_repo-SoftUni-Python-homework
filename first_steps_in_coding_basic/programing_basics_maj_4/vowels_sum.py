text = input() .lower()
total_sum = 0

for c in text:
    if c == "a":
        total_sum += 1
    elif c == "e":
        total_sum += 2
    elif c == "i":
        total_sum += 3
    elif c == "o":
        total_sum += 4
    elif c == "u":
        total_sum += 5
print(total_sum)









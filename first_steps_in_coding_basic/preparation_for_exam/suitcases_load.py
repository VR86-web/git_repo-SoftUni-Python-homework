trunk_capacity = float(input())
suitcase_count = 0
while True:
    command = input()
    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    suitcase_volume = float(command)
    suitcase_count += 1
    if suitcase_count % 3 == 0:
        suitcase_volume += suitcase_volume * 0.10
    if suitcase_volume > trunk_capacity:
        print("No more space!")
        suitcase_count -= 1
        break
    trunk_capacity -= suitcase_volume
print(f"Statistic: {suitcase_count} suitcases loaded.")


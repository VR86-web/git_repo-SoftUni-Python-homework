import re

string = input()
pattern = r'(=|\/)([A-Z][A-Za-z]{2,})(\1)'
matches = re.findall(pattern, string)

destination = []
travel_points = 0
for match in matches:
    destination.append(match[1])
    travel_points += len(match[1])
print(f"Destinations: {', '.join(destination)}")
print(f"Travel Points: {travel_points}")
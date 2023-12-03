import re

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
bought_furniture = []
total_cost = 0
data = input()
while data != "Purchase":
    match = re.search(pattern, data)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
    data = input()
print(f"Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
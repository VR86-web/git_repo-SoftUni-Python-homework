quantity_of_decorations = int(input())
days_till_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_gerland_price = 3
tree_lights_price = 15
total_cost = 0
total_spirit = 0
for days in range(1, days_till_christmas + 1):
    if days % 11 == 0:
        quantity_of_decorations += 2
    if days % 2 == 0:
        total_cost += quantity_of_decorations * ornament_set_price
        total_spirit += 5
    if days % 3 == 0:
        total_cost += quantity_of_decorations * (tree_skirt_price + tree_gerland_price)
        total_spirit += 10 + 3
    if days % 5 == 0:
        total_cost += quantity_of_decorations * tree_lights_price
        total_spirit += 17
        if days % 3 == 0:
            total_spirit += 30
    if days % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_gerland_price + tree_lights_price
if days_till_christmas % 10 == 0:
    total_spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
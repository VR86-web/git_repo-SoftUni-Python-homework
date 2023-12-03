items = {"shards": 0, "fragments": 0, "motes": 0}
legendary_items = input().split()
obtained = False
while not obtained:
    for index in range(0, len(legendary_items), 2):
        value = int(legendary_items[index])
        key = legendary_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    legendary_items = input().split()
for material, quantity in items.items():
    print(f"{material}: {quantity}")
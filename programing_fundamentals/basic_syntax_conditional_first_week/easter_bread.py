budget = float(input())
price_per_kg_flour = float(input())
loaf_bread_counter = 0
colored_eggs_counter = 0
price_per_pack_of_eggs = price_per_kg_flour * 0.75
price_per_litter_milch = price_per_kg_flour * 1.25
price_per_one_loaf = price_per_kg_flour + price_per_pack_of_eggs + (price_per_litter_milch / 4)
while budget >= price_per_one_loaf:
    budget -= price_per_one_loaf
    loaf_bread_counter += 1
    colored_eggs_counter += 3
    if loaf_bread_counter % 3 == 0:
        colored_eggs_counter -= (loaf_bread_counter - 2)
print(f"You made {loaf_bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {budget:.2f}BGN left.")
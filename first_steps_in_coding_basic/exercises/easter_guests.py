from math import ceil
guest_number = int(input())
budget = int(input())
one_egg = 0.45
one_easter_bread = 4
needed_easter_breads = ceil(guest_number / 3)
needed_eggs = guest_number * 2
total_price = needed_easter_breads * one_easter_bread + needed_eggs * one_egg
difference = abs(total_price - budget)
if budget >= total_price:
    print(f"Lyubo bought {needed_easter_breads} Easter bread and {needed_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
from math import ceil

budget = float(input())
number_of_students = int(input())
flour_price_per_pack = float(input())
one_egg_price = float(input())
one_apron_price = float(input())
apron_needed = ceil(number_of_students * 1.2) * one_apron_price
eggs_needed = one_egg_price * 10 * number_of_students
flour_package = number_of_students - number_of_students // 5
flour_needed = flour_price_per_pack * flour_package
current_budget = apron_needed + eggs_needed + flour_needed
needed_budget = abs(current_budget - budget)
if current_budget <= budget:
    print(f"Items purchased for {current_budget:.2f}$.")
else:
    print(f"{needed_budget:.2f}$ more needed.")
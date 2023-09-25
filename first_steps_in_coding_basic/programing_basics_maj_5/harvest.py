from math import floor, ceil

vineyard_area = int(input())
kilos_grape_per_square_meter = float(input())
needed_liters_wine = int(input())
number_of_workers = int(input())
total_kilos_grape = vineyard_area * kilos_grape_per_square_meter
kilos_for_producing_wine = total_kilos_grape * 0.4
total_liters_wine = kilos_for_producing_wine / 2.5
different = abs(total_liters_wine - needed_liters_wine)
wine_per_one_worker = different / number_of_workers
if total_liters_wine < needed_liters_wine:
    print(f"It will be a tough winter! More {floor(different)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(total_liters_wine)} liters.")
    print(f"{ceil(different)} liters left -> {ceil(wine_per_one_worker)} liters per person.")



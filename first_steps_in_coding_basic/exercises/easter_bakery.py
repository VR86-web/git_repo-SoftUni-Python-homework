flour_price_per_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
number_of_crusts_and_egs = int(input())
yeast_packets = int(input())
sugar_kg_price = flour_price_per_kg * 0.75
crusts_and_egs_price = flour_price_per_kg * 1.1
yeast_price = sugar_kg_price * 0.2
total_price = flour_price_per_kg * flour_kg \
              + sugar_kg_price * sugar_kg \
              + number_of_crusts_and_egs * crusts_and_egs_price \
              + yeast_packets * yeast_price
print(f"{total_price:.2f}")

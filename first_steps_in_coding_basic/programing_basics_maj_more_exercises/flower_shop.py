from math import floor, ceil

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
price_for_present = float(input())

total_price = number_of_magnolias * 3.25 \
              + number_of_hyacinths * 4 \
              + number_of_roses * 3.5 \
              + number_of_cacti * 8
price_after_taxes = total_price - total_price * 0.05
difference = abs(price_for_present - price_after_taxes)
if price_for_present <= price_after_taxes:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")

number_of_easter_bread = int(input())
number_of_cartoon_egs = int(input())
kilograms_cookies = int(input())
price_per_easter_bread = 3.2
price_per_cartoon_egs = 4.35
price_per_kilogram_cookies = 5.4
price_of_egg_paint_for_one_egg = 0.15
price_of_total_egg_paint = 0.15 * 12
total_lunch_price = number_of_easter_bread * price_per_easter_bread \
                    + number_of_cartoon_egs * price_per_cartoon_egs \
                    + number_of_cartoon_egs * price_of_total_egg_paint \
                    + kilograms_cookies * price_per_kilogram_cookies
print(f"{total_lunch_price:.2f}")
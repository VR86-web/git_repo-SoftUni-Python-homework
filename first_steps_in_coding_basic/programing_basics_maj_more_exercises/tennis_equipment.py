from math import ceil, floor

price_per_tennis_racket = float(input())
num_of_tennis_rackets = int(input())
num_of_sneakers = int(input())
price_per_sneakers = price_per_tennis_racket / 6
rest_equipment = (price_per_tennis_racket * num_of_tennis_rackets \
                 + price_per_sneakers * num_of_sneakers) * 0.2
total_price = price_per_tennis_racket * num_of_tennis_rackets \
              + price_per_sneakers * num_of_sneakers \
              + rest_equipment
price_to_be_paid_by_djokovic = floor(total_price / 8)
price_to_be_paid_by_sponsors = ceil(total_price * 7/8)
print(f"Price to be paid by Djokovic {price_to_be_paid_by_djokovic}")
print(f"Price to be paid by sponsors {price_to_be_paid_by_sponsors}")

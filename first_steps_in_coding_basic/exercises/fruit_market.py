strawberries_price = float(input())
quantity_bananas = float(input())
quantity_oranges = float(input())
quantity_raspberries = float(input())
quantity_strawberries = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2
total_price = strawberries_price * quantity_strawberries + raspberries_price * quantity_raspberries \
              + oranges_price * quantity_oranges \
              + bananas_price * quantity_bananas
print(f'{total_price:.2f}')

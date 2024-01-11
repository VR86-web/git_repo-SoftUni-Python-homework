number_of_orders = int(input())
total_price = 0
for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    coffee_price = capsules_per_day * days * price_per_capsule
    print(f"The price for the coffee is: ${coffee_price:.2f}")
    total_price += coffee_price
print(f"Total: ${total_price:.2f}")
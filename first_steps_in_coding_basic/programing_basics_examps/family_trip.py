budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_additional_costs = int(input())

money_for_additional_costs = budget * percent_additional_costs / 100

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05
needed_money_for_staying = number_of_nights * price_per_night
total_needed_money = needed_money_for_staying + money_for_additional_costs
different = abs(budget - total_needed_money)
if budget >= total_needed_money:
    print(f"Ivanovi will be left with {different:.2f} leva after vacation.")
else:
    print(f"{different:.2f} leva needed.")
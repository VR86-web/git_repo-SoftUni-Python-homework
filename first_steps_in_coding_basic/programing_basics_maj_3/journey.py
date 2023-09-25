budget = float(input())
season = input()

destination = ""
type_of_holiday = ""
money_spend = 0
if season == "summer":
    type_of_holiday = "Camp"
    if budget <= 100:
        money_spend = budget * 0.3
        destination = "Bulgaria"
    elif budget <= 1000:
        money_spend = budget * 0.4
        destination = "Balkans"
    elif budget > 1000:
        type_of_holiday = "Hotel"
        money_spend = budget * 0.9
        destination = "Europe"
elif season == "winter":
    type_of_holiday = "Hotel"
    if budget <= 100:
        money_spend = budget * 0.7
        destination = "Bulgaria"
    elif budget <= 1000:
        money_spend = budget * 0.8
        destination = "Balkans"
    elif budget > 1000:
        money_spend = budget * 0.9
        destination = "Europe"
print(f"Somewhere in {destination}")
print(f"{type_of_holiday} - {money_spend:.2f}")


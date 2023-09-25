term_of_contract = input()
type_of_contract = input()
added_mobile_internet = input()
number_of_months_for_paying = int(input())
price = 0
if term_of_contract == "one":
    if type_of_contract == "Small":
        price = 9.98
    elif type_of_contract == "Middle":
        price = 18.99
    elif type_of_contract == "Large":
        price = 25.98
    elif type_of_contract == "ExtraLarge":
        price = 35.99
elif term_of_contract == "two":
    if type_of_contract == "Small":
        price = 8.58
    elif type_of_contract == "Middle":
        price = 17.09
    elif type_of_contract == "Large":
        price = 23.59
    elif type_of_contract == "ExtraLarge":
        price = 31.79
if added_mobile_internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85
if term_of_contract == "two":
    price -= price * 0.0375
total_price = price * number_of_months_for_paying
print(f"{total_price:.2f} lv.")
stage_of_championship = input()
ticket_type = input()
number_of_tickets = int(input())
picture_with_trophy = input()
price_counter = 0
price_for_picture_with_trophy = 0
total_price = 0
if stage_of_championship == "Quarter final":
    if ticket_type == "Standard":
        price_counter += 55.50
    elif ticket_type == "Premium":
        price_counter += 105.20
    elif ticket_type == "VIP":
        price_counter += 118.90
elif stage_of_championship == "Semi final":
    if ticket_type == "Standard":
        price_counter += 75.88
    elif ticket_type == "Premium":
        price_counter += 125.22
    elif ticket_type == "VIP":
        price_counter += 300.40
elif stage_of_championship == "Final":
    if ticket_type == "Standard":
        price_counter += 110.10
    elif ticket_type == "Premium":
        price_counter += 160.66
    elif ticket_type == "VIP":
        price_counter += 400
if picture_with_trophy == 'Y':
    price_for_picture_with_trophy = number_of_tickets * 40
current_price = number_of_tickets * price_counter
if current_price <= 2500:
    total_price = current_price + price_for_picture_with_trophy
elif 2500 < current_price <= 4000:
    current_price = current_price * 0.9
    total_price = current_price + price_for_picture_with_trophy
elif current_price > 4000:
    current_price = current_price * 0.75
    total_price = current_price
print(f"{total_price:.2f}")
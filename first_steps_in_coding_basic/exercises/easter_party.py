guest_number = int(input())
envelope_price_per_person = float(input())
desi_budget = float(input())
envelope_price_counter = 0
if guest_number < 10:
    envelope_price_counter = envelope_price_per_person
if 10 <= guest_number <= 15:
    envelope_price_counter = envelope_price_per_person * 0.85
elif 15 < guest_number <= 20:
    envelope_price_counter = envelope_price_per_person * 0.8
elif guest_number > 20:
    envelope_price_counter = envelope_price_per_person * 0.75
birthday_cake = desi_budget * 0.1
total_price = guest_number * envelope_price_counter + birthday_cake
difference = abs(total_price - desi_budget)
if desi_budget >= total_price:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
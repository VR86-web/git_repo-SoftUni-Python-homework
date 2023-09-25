name_of_city = input()
type_of_packet = input()
vip_discount = input()
days_of_staying = int(input())
price_per_day = 0
if days_of_staying > 7:
    days_of_staying -= 1
if not (name_of_city in ("Bansko", "Borovets") and type_of_packet in ("withEquipment", "noEquipment")) \
        and not (name_of_city in ("Varna", "Burgas" ) and type_of_packet in ("withBreakfast", "noBreakfast")):
    print("Invalid input!")
elif days_of_staying < 1:
    print("Days must be positive number!")
else:
    if name_of_city == "Bansko" or name_of_city == "Borovets":
        if type_of_packet == "withEquipment":
            price_per_day = 100 * days_of_staying
            if vip_discount == "yes":
                price_per_day *= 0.9
        elif type_of_packet == "noEquipment":
            price_per_day = 80 * days_of_staying
            if vip_discount == "yes":
                price_per_day *= 0.95
    elif name_of_city == "Varna" or name_of_city == "Burgas":
        if type_of_packet == "withBreakfast":
            price_per_day = 130 * days_of_staying
            if vip_discount == "yes":
                price_per_day *= 0.88
        elif type_of_packet == "noBreakfast":
            price_per_day = 100 * days_of_staying
            if vip_discount == "yes":
                price_per_day *= 0.93
    print(f"The price is {price_per_day:.2f}lv! Have a nice time!")



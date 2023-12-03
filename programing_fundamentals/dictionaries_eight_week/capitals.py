country_names = input().split(", ")
city_names = input().split(", ")

country_capital = {country_names[index]: city_names[index] for index in range(0, len(country_names))}
for country_names, city_names in country_capital.items():
    print(f"{country_names} -> {city_names}")


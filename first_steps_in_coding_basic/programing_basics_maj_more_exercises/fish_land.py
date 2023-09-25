price_per_kilo_mackerel_fish = float(input())
price_per_kilo_sprat_fish = float(input())
kilo_bonito_fish = float(input())
kilo_scad_fish = float(input())
kilo_mussels = float(input())

price_per_kilo_bonito_fish = price_per_kilo_mackerel_fish + (price_per_kilo_mackerel_fish * 0.6)
price_per_kilo_scad_fish = price_per_kilo_sprat_fish + (price_per_kilo_sprat_fish * 0.8)
price_per_kilo_mussels = 7.5

total_sum = kilo_bonito_fish * price_per_kilo_bonito_fish \
            + kilo_scad_fish * price_per_kilo_scad_fish \
            + kilo_mussels * price_per_kilo_mussels
print(f"{total_sum:.2f}")
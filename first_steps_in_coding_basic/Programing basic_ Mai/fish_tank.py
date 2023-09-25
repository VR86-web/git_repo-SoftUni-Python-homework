lengt = int(input())
widht = int(input())
height = int(input())
percent_non_free_volume = float(input())
fish_tank_volume_in_centimeters = lengt * widht * height
fish_tank_volume_in_litres = fish_tank_volume_in_centimeters * 0.001
percentage = percent_non_free_volume * 0.01
needed_liters = fish_tank_volume_in_litres * (1 - percentage)
print(needed_liters)

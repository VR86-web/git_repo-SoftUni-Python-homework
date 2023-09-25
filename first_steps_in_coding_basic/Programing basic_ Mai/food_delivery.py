num_chicken_menu = int(input())
num_fish_menu = int(input())
num_vegetarian_menu = int(input())
chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
total_sum = num_chicken_menu * chicken_menu \
            + num_fish_menu * fish_menu \
            + num_vegetarian_menu * vegetarian_menu
dessert = total_sum * 0.2
delivery_price = 2.50
final_price = total_sum + dessert + delivery_price
print(final_price)

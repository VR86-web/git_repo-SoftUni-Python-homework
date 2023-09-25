price_per_kilo_vegetables = float(input())
price_per_kilo_fruits = float(input())
weight_of_vegetables = int(input())
weight_of_fruits = int(input())
total_sum = price_per_kilo_vegetables * weight_of_vegetables \
            + price_per_kilo_fruits * weight_of_fruits
final_price = total_sum / 1.94
formatted_final_price = format(final_price, '.2f')
print(formatted_final_price)

number_of_pens = int(input())
number_of_markers = int(input())
liters_of_detergent = int(input())
percent_discount = int(input())
price_per_pens = 5.8
price_per_markers = 7.2
price_per_detergent = 1.2
needed_sum = number_of_pens * price_per_pens \
             + number_of_markers * price_per_markers \
             + liters_of_detergent * price_per_detergent
needed_sum = needed_sum - needed_sum * (percent_discount / 100)
print(needed_sum)
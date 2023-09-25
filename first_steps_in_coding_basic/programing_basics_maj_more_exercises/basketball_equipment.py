price_per_year_for_basket_training = int(input())
basketball_sneakers = price_per_year_for_basket_training * 0.6
basketball_dress = basketball_sneakers * 0.8
basketball_ball = basketball_dress / 4
basketball_accessories = basketball_ball / 5
total_expenses = price_per_year_for_basket_training \
                 + basketball_sneakers \
                 + basketball_dress \
                 + basketball_ball \
                 + basketball_accessories
print(f"{total_expenses:.2f}")
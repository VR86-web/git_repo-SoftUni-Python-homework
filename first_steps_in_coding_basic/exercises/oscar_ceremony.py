rent_for_hall = int(input())

statuette = rent_for_hall - rent_for_hall * 0.30
catering = statuette - statuette * 0.15
voicing = catering / 2

total_expenses = rent_for_hall + statuette + catering + voicing

print(f"{total_expenses:.2f}")
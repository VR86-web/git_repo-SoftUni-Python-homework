import random
# user_id = "1234"
# money_balance_about_last_month = 5000
# counter = 0
print("Welcome to the Slot Machine Game !")

symbols = ["🍒", "🍉", "🍈", "🍇", "🍓","🍌"]

balance = int(input("Enter Your initial balance:"))
bet = 0
while balance > 0:
    print(30 * '-')
    print("Current Balance:", balance)
    while True:
        bet = int(input("Enter Your bet amount (0 ti exit): "))
        if bet == 0:
            break
        if bet > balance:
            print("Insufficient balance. Please a lower bet!")
        else:
            break
    if bet == 0:
        break
    balance -= bet
#   money_balance_about_last_month += bet
    print("Spinning the reels...")
    reel1 = random.choice(symbols)
    reel2 = random.choice(symbols)
    reel3 = random.choice(symbols)

 #   if user_id == "1234" and money_balance_about_last_month > 5000:
#        print(reel1, reel1, reel1)
#        balance += bet * 10
#        print("Congratulations! You won", bet * 10, "money!")
#       continue
    print(reel1, reel2, reel3)

    if reel1 == reel2 == reel3:
        winnings = bet * 10
        balance += winnings
        print("Congratulations! You won", winnings, "money!")
    elif reel1 == reel2 or reel2 == reel3:
        winnings = bet * 2
        balance += winnings
        print("Congratulations! You won", winnings, "money!")
    else:
        print("Sorry! No match. Better luck next time!")

print("Game over. Final balance:", balance)

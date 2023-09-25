destination = input()

while destination != "End":
    budget = float(input())
    needed_money = 0
    while budget > needed_money:
        savings = float(input())
        needed_money += savings
    print(f"Going to {destination}!")
    destination = input()
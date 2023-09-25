destination = input()
budget = savings = 0

while destination != "End":
    budget = float(input())
    if budget > 0:
        while budget > savings:
            money = float(input())
            if money > 0:
                savings += money
                if savings >= budget:
                    print(f"Going to {destination}!")
                    savings = 0
            if savings == 0:
                break
    destination = input()



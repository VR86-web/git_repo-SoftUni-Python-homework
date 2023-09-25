budget_for_actors = float(input())
actor_name = input()

while actor_name != "ACTION":
    if len(actor_name) <= 15:
        salary = float(input())
    else:
        salary = budget_for_actors * 0.2
    budget_for_actors -= salary
    if budget_for_actors <= 0:
        print(f"We need {abs(budget_for_actors):.2f} leva for our actors.")
        break
    actor_name = input()
if budget_for_actors > 0:
    print(f"We are left with {budget_for_actors:.2f} leva.")
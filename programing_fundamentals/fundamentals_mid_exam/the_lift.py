people_waiting_for_the_lift = int(input())
current_state_of_the_lift = [int(current_state) for current_state in input().split()]
for places in range(len(current_state_of_the_lift)):
    can_load = min(4 - current_state_of_the_lift[places], people_waiting_for_the_lift)
    current_state_of_the_lift[places] += can_load
    people_waiting_for_the_lift -= can_load
if people_waiting_for_the_lift > 0:
    print(f"There isn't enough space! {people_waiting_for_the_lift} people in a queue!")
elif len([card for card in current_state_of_the_lift if card < 4]) > 0:
    print("The lift has empty spots!")
print(" ".join([str(cart) for cart in current_state_of_the_lift]))

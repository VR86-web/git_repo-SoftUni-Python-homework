from sys import maxsize

best_score = -maxsize
current_name = ""
best_player = ""
player_name = input()
while player_name != "END":
    goal = int(input())
    current_name = player_name
    if goal > best_score:
        best_score = goal
        best_player = current_name
    if goal >= 10:
        break
    player_name = input()
print(f"{best_player} is the best player!")
if best_score >= 3:
    print(f"He has scored {best_score} goals and made a hat-trick !!!")
elif best_score < 3:
    print(f"He has scored {best_score} goals.")
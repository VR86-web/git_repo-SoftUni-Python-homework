from sys import maxsize
player_name = input()
max_value = -maxsize
winner_name = ""
while player_name != "Stop":
    current_score = 0
    for letter in player_name:
        number = int(input())
        if number == ord(letter):
            current_score += 10
        else:
            current_score += 2
        if current_score >= max_value:
            max_value = current_score
            winner_name = player_name
    player_name = input()
print(f"The winner is {winner_name} with {max_value} points!")










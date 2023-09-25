length_of_cake = int(input())
width_of_cake = int(input())
total_pieces_cake = length_of_cake * width_of_cake
cake_finish = False
command = input()
while command != "STOP":
    number_of_pieces_cake = int(command)
    total_pieces_cake -= number_of_pieces_cake
    if total_pieces_cake < 0:
        cake_finish = True
        break
    command = input()
if cake_finish:
    print(f"No more cake left! You need {abs(total_pieces_cake)} pieces more.")
else:
    print(f"{total_pieces_cake} pieces are left.")

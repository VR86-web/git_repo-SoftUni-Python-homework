budget = float(input())
num_of_video_cards = int(input())
num_of_processors = int(input())
num_of_ram_memory = int(input())
one_video_card = 250
video_card_price = one_video_card * num_of_video_cards
one_processor = video_card_price * 0.35
one_ram_memory = video_card_price * 0.10
total_sum = video_card_price \
            + num_of_processors * one_processor \
            + num_of_ram_memory * one_ram_memory

if num_of_video_cards > num_of_processors:
    total_sum *= 0.85
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You have {budget - total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")

cards = input().split()
count_of_faro_shuffles = int(input())
for shuffles in range(count_of_faro_shuffles):
    middle_deck = len(cards) // 2
    left_part_deck = cards[:middle_deck]
    right_part_deck = cards[middle_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part_deck)):
        deck_after_shuffling.append(left_part_deck[card_index])
        deck_after_shuffling.append(right_part_deck[card_index])
    cards = deck_after_shuffling
print(cards)

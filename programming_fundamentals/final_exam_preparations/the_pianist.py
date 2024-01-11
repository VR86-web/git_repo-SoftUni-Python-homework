number_of_pieces = int(input())
piano_pieces_dict = {}
for pieces in range(number_of_pieces):
    piece, composer, key = input().split("|")
    piano_pieces_dict[piece] = {'composer': composer, 'key': key}

while True:
    command = input()
    if command == "Stop":
        break
    tokens = command.split("|")
    action = tokens[0]
    piece = tokens[1]
    if action == "Add":
        composer, key = tokens[2], tokens[3]
        if piece not in piano_pieces_dict:
            piano_pieces_dict[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif action == "Remove":
        if piece in piano_pieces_dict:
            del piano_pieces_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif action == "ChangeKey":
        new_key = tokens[2]
        if piece in piano_pieces_dict:
            piano_pieces_dict[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, data in piano_pieces_dict.items():
    print(f"{piece} -> Composer: {data['composer']}, Key: {data['key']}")
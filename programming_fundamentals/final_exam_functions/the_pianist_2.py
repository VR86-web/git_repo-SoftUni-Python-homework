def add(data, current_piece, current_composer, current_key):
    if current_piece not in data:
        data[current_piece] = {"composer": current_composer, "key": current_key}
        print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
        return data
    else:
        print(f"{current_piece} is already in the collection!")
        return data


def remove(data, current_piece):
    if current_piece in data:
        del data[current_piece]
        print(f"Successfully removed {current_piece}!")
        return data
    else:
        print(f"Invalid operation! {current_piece} does not exist in the collection.")
        return data


def change_key(data, current_piece, new_current_key):
    if current_piece in data:
        data[current_piece]["key"] = new_current_key
        print(f"Changed the key of {current_piece} to {new_current_key}!")
        return data
    else:
        print(f"Invalid operation! {current_piece} does not exist in the collection.")
        return data


number_of_pieces = int(input())
piano_pieces_dict = {}
for number in range(number_of_pieces):
    piece, composer, key = input().split("|")
    piano_pieces_dict[piece] = {"composer": composer, "key": key}

command = input()
while command != "Stop":
    tokens = command.split("|")
    action = tokens[0]
    if action == "Add":
        piece = tokens[1]
        composer = tokens[2]
        key = tokens[3]
        piano_pieces_dict = add(piano_pieces_dict, piece, composer, key)

    elif action == "Remove":
        piece = tokens[1]
        piano_pieces_dict = remove(piano_pieces_dict, piece)

    elif action == "ChangeKey":
        piece = tokens[1]
        new_key = tokens[2]
        piano_pieces_dict = change_key(piano_pieces_dict, piece, new_key)

    command = input()
for key, value in piano_pieces_dict.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")
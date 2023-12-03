def process_to_do_notes():
    to_do_list = []

    while True:
        notes = input()

        if notes == "End":
            break
        to_do_list.append(notes)
    sorted_notes = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
    return [notes.split("-")[1] for notes in sorted_notes]


result = process_to_do_notes()
print(result)

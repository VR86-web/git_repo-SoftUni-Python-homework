letter_from_a_to_z = input()
letter_from_first_letter_to_z = input()
letter_from_a_to_z_without = input()

combinations = 0
for start_letter in range(ord(letter_from_a_to_z), ord(letter_from_first_letter_to_z) + 1):
    if start_letter == ord(letter_from_a_to_z_without):
        continue
    for final_letter in range(ord(letter_from_a_to_z), ord(letter_from_first_letter_to_z) + 1):
        if final_letter == ord(letter_from_a_to_z_without):
            continue
        for exception in range(ord(letter_from_a_to_z), ord(letter_from_first_letter_to_z) + 1):
            if exception == ord(letter_from_a_to_z_without):
                continue
            combinations += 1
            print(f"{chr(start_letter)}{chr(final_letter)}{chr(exception)}", end=" ")
print(combinations)

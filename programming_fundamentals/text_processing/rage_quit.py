text = input()
unique_symbols = ""
repetitions = ""
current_symbol = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index].upper()
    else:
        for next_symbol in range(index, len(text)):
            if not text[next_symbol].isdigit():
                break
            repetitions += text[next_symbol]
        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)
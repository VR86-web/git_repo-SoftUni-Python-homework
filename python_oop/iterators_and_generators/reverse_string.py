def reverse_text(string):
    start_idx = len(string) - 1
    end_idx = 0
    while start_idx >= end_idx:
        yield string[start_idx]
        start_idx -= 1


for char in reverse_text("step"):
    print(char, end='')

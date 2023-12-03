word = input()
sequence = input()
while word in sequence:
    sequence = sequence.replace(word, "")
print(sequence)
most_powerful_word = ""
most_powerful_word_ascii_counter = 0


while True:
    word = input()
    if word == "End of words":
        break
    current_word_counter = 0
    for letter in word:
        current_word_counter += ord(letter)
    if word[0].lower() in "aeiouy":
        current_word_counter *= len(word)
    else:
        current_word_counter = int(current_word_counter / len(word))
    if current_word_counter > most_powerful_word_ascii_counter:
        most_powerful_word = word
        most_powerful_word_ascii_counter = current_word_counter
print(f"The most powerful word is {most_powerful_word} - {most_powerful_word_ascii_counter}")


the_most_powerful_word = ""
the_most_powerful_ascii_score = 0

while True:
    word = input()
    if word == "End of words":
        break
    current_word_counter = 0
    for text in word:
        current_word_counter += ord(text)
    if word[0].lower() in "aeiouy":
        current_word_counter *= len(word)
    else:
        current_word_counter = int(current_word_counter / len(word))
    if current_word_counter > the_most_powerful_ascii_score:
        the_most_powerful_word = word
        the_most_powerful_ascii_score = current_word_counter
print(f"The most powerful word is {the_most_powerful_word} - {the_most_powerful_ascii_score}")

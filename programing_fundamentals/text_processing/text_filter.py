banned_words = input().split(", ")
text = input()
for word in banned_words:
    word_count = "*" * len(word)
    text = text.replace(word, word_count)
print(text)

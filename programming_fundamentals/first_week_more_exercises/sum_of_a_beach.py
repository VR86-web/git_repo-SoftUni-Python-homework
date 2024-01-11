word = input()
word = word.lower()
word_list = ["sand", "water", "fish", "sun"]
counter = 0
for item in word_list:
    if item in word:
        item_counter = word.count(item)
        counter += item_counter
print(counter)

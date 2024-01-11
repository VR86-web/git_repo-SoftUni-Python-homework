import re

text_string = input()
pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-za-z]{3,})(\1)'
matches = re.findall(pattern, text_string)
mirror_words = []
count_of_words = len(matches)
for pair in matches:
    if pair[1] == pair[3][::-1]:
        mirror_words.append(f"{pair[1]} <=> {pair[3]}")
if count_of_words > 0:
    print(f"{count_of_words} word pairs found!")
    if not mirror_words:
        print("No mirror words!")
    else:
        print("The mirror words are: ")
        print(', '.join(mirror_words))

else:
    print("No word pairs found!")
    print("No mirror words!")
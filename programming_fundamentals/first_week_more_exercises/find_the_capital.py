word = input()
index_list = []
for letter in range(len(word)):
   if word[letter].isupper():
        index_list.append(letter)
print(index_list)


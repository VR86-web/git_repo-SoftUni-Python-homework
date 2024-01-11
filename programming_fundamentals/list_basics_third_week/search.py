number = int(input())
magic_word = input()
word_list = []

for num in range(number):
    words = input()
    word_list.append(words)
print(word_list)
magic_word_list = []
for current_word in word_list:
    if magic_word in current_word:
        magic_word_list.append(current_word)
print(magic_word_list)
words_needed = input().split(", ")
words_list = input().split(", ")
needed_words_list = []
for words_needed_string in words_needed:
    for words_list_string in words_list:
        if words_needed_string in words_list_string:
            needed_words_list.append(words_needed_string)
            break
print(needed_words_list)

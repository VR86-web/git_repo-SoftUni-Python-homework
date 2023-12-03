def palindrome_words(word):
    if word == word[::-1]:
        return word


words = input().split()
palindromes = input()
palindrome_list = [word for word in words if palindrome_words(word)]
palindrome_counter = palindrome_list.count(palindromes)
print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")
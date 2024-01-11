words = input().split()
palindrome = input()
palindrome_list = []
for current_word in words:
    if current_word == current_word[::-1]:
        palindrome_list.append(current_word)
number_of_palindromes = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {number_of_palindromes} times")

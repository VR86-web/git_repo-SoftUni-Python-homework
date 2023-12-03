text = input()
result = [letters for letters in text if letters.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(result))
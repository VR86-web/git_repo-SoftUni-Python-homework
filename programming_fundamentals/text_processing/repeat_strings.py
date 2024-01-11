strings = input().split(" ")
repeated_string = ""
for string in strings:
    repeated_string += string * len(string)
print(repeated_string)
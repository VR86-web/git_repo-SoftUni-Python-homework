import re

numbers = input()
regex = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
match = re.findall(regex, numbers)
print(", ".join(match))
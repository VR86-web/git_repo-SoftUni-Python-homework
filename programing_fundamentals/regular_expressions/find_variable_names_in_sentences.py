import re

sentence = input()
pattern = r'\b\_([A-Za-z0-9]+)\b'
variables = re.findall(pattern, sentence)
print(",".join(variables))
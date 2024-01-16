
sequence_of_parentheses = input()
matches = {"(": ")",
           "{": "}",
           "[": "]"
           }

is_balanced = True
start_parenthesis = []
for element in sequence_of_parentheses:
    if element in "({[":
        start_parenthesis.append(element)
    elif not start_parenthesis:
        is_balanced = False
    else:
        current_start_parenthesis = start_parenthesis.pop()
        if matches[current_start_parenthesis] != element:
            is_balanced = False
    if not is_balanced:
        break

if is_balanced:
    print("YES")
else:
    print("NO")







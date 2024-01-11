parentheses = input()

matching_start_of_parentheses = []
for index in range(len(parentheses)):
    if parentheses[index] == "(":
        matching_start_of_parentheses.append(index)
    elif parentheses[index] == ")":
        end_index = index + 1
        start_index = matching_start_of_parentheses.pop()
        print(parentheses[start_index:end_index])
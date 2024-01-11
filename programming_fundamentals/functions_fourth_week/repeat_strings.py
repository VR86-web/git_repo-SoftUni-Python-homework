repeat_string = lambda string, number : string * number


string = input()
number = int(input())
result = repeat_string(string, number)
print(result)
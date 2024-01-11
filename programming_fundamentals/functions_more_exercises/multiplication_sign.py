def multiplication(integers):
    result = ""
    negative_numbers = 0
    positive_numbers = 0
    for integer in integers:
        if integer == 0:
            result = "zero"
            break
        elif integer < 0:
            negative_numbers += 1
        else:
            positive_numbers += 1
        if negative_numbers % 2 == 0:
            result = "positive"
        else:
            result = "negative"
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())
list_of_integers = [first_number, second_number, third_number]
print(multiplication(list_of_integers))
def some_numbers(numbers):
    sum_negative = sum(num for num in numbers if num < 0)
    sum_positive = sum(num for num in numbers if num > 0)

    print(sum_negative)
    print(sum_positive)

    if sum_positive > abs(sum_negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


nums = [int(x) for x in input().split()]

some_numbers(nums)

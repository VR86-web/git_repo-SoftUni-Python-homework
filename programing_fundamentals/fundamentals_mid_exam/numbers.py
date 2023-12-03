def top_5(numbers):
    average_value = sum(numbers) / len(numbers)
    current_sum = [current_numbers for current_numbers in sorted(numbers, reverse=True)
                   if current_numbers > average_value]
    if len(current_sum) != 0:
        return " ".join(map(str, current_sum[:5]))
    else:
        return "No"


nums = list(map(int, input().split()))
print(top_5(nums))

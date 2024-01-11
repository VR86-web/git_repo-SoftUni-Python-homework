money_for_beggars = input().split(",")
count_of_beggars = int(input())
sum_per_beggar = []
for money in money_for_beggars:
    sum_per_beggar.append(int(money))
final_sums = []
start_index = 0
while start_index < count_of_beggars:
    current_beggar_sum = 0
    for beggar in range(start_index, len(sum_per_beggar), count_of_beggars):
        current_beggar_sum += sum_per_beggar[beggar]
    final_sums.append(current_beggar_sum)
    start_index += 1
print(final_sums)
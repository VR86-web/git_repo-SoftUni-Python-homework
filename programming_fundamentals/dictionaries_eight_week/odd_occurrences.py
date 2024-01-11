words = input().split()
dict_data = {}
list_results = []
for item in words:
    if item.lower() in dict_data:
        dict_data[item.lower()] += 1
    else:
        dict_data[item.lower()] = 1

for item in dict_data:
    if dict_data[item] % 2 != 0:
        list_results.append(item)
print(" ".join(list_results))
strings_line = input().split()
while True:
    command = input().split()
    if command[0] == "3:1":
        break
    elif command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(strings_line) - 1:
            end_index = len(strings_line) - 1
        merged_elements = "".join(strings_line[start_index:end_index+1])
        strings_line[start_index:end_index + 1] = [merged_elements]
    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        element = strings_line[index]
        divided_partition = []
        partition_length = len(element) // partitions
        for current_element in range(partitions):
            if current_element != partitions - 1:
                divided_partition.append(element[current_element * partition_length:(current_element + 1) * partition_length])
            else:
                divided_partition.append(element[current_element * partition_length:])
        strings_line[index:index+1] = divided_partition
print(" ".join(strings_line))






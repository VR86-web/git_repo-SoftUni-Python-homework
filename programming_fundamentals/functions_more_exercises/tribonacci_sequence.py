
def tribonacci_sequence(def_num):
    sequence = [1]
    for index in range(1, def_num):
        if len(sequence) < 3:
            sequence.append(index)
        else:
            sequence.append(sum(sequence[-3:]))
    return " ".join([str(num) for num in sequence])


number = int(input())
print(tribonacci_sequence(number))
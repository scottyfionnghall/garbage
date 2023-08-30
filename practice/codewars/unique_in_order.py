def unique_in_order(sequence):
    unique = []
    for i in range(0, len(sequence)):
        if i+1 < len(sequence):
            if sequence[i] != sequence[i+1]:
                unique.append(sequence[i])
        else:
            unique.append(sequence[i])
    return unique


print(unique_in_order([1, 2, 2, 3, 3]))

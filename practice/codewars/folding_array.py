def fold_array(array,runs):
    for run in range(runs):
        middle = len(array)//2
        if len(array) != 2:
            if len(array) % 2 == 0:
                first_part = array[:middle]
                second_part = array[middle:]
            else:
                first_part = array[:middle+1]
                second_part = array[middle+1:]
            second_part = list(reversed(second_part))
            for i in range(len(second_part)):
                first_part[i] = first_part[i] + second_part[i]
                array = first_part[:]
        else:
            first_part = array[0]
            second_part = array[1]
            array = []
            array.append(first_part+second_part)
    return(array)

print(fold_array([1, 2, 3, 4, 5],1))
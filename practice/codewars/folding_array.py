def fold_array(array,runs):
    # make a copy of an array
    current_array = array[:]
    # make a for loop for every run
    for run in range(runs):
        # get the middle of an array to use as a length of the answer
        middle = len(current_array)//2
        # for every item in a array, take last item, add it to the first and remove it
        for i in range(middle):
            current_array[i] += current_array.pop()
    return(current_array)

print(fold_array([1,2,3,4,5],2))
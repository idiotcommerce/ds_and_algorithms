

def dup(array):

    without_duplicates = []

    if len(array) < 2:
        return array

    for item in array:
        if  without_duplicates == [] or item != without_duplicates[-1]:
            without_duplicates.append(item)
    print(without_duplicates)



print(dup([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6]))



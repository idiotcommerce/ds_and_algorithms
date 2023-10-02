
 # delete duplicates in sorted array

# O(n) time complexity and O(1) space complexity 

def delete_duplicates(array):
    starting_index = 0
    rotating_index = 1
    high = len(array)-1

    if high < 2:
        return array

    for x in range(high):
        if starting_index > high:
            break

        else :
            if array[starting_index]== array[rotating_index]:
                array.pop(rotating_index)
                high -= 1
            elif array[starting_index] < array[rotating_index]:
                starting_index += 1
                rotating_index += 1

    return array

print(delete_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6]))



# O(n) time O(n) space 


def dup(array):

    without_duplicates = []

    if len(array) < 2:
        return array

    for item in array:
        if  without_duplicates == [] or item != without_duplicates[-1]:
            without_duplicates.append(item)
    print(without_duplicates)


print(dup([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6]))





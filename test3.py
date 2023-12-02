
# two numbeer sum

def two_number_sum(numbers, target):
    sum = []
    dictionary = {}

    for item in range(len(numbers)):
        competent = target - item
        if competent in dictionary:
            print(f' pair sum is ( {item} and {competent})')
        dictionary[numbers[item]] = numbers[item]



print(two_number_sum([8, 5 , 7, 3, 1, 2], 10))



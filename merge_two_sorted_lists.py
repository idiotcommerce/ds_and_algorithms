
# nerge two sorted lists


def merge_two_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    for _ in range(len(list1) + len(list2)):

        if i < len(list1) and (j >= len(list2) or list1[i] < list2[j]):
            merged_list.append(list1[i])
            i += 1
            
        else:
            merged_list.append(list2[j])
            j += 1

    return merged_list

print(merge_two_sorted_lists([3, 5, 6, 10], [1, 2, 7, 8, 11, 12]))














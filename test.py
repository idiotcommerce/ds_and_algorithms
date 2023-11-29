
# delete duplicates in sorted array

# # O(n) time complexity and O(1) space complexity 

# def delete_duplicates(array):
#     starting_index = 0
#     rotating_index = 1
#     high = len(array)-1

#     if high < 2:
#         return array

#     for x in range(high):
#         if starting_index > high:
#             break

#         else :
#             if array[starting_index]== array[rotating_index]:
#                 array.pop(rotating_index)
#                 high -= 1
#             elif array[starting_index] < array[rotating_index]:
#                 starting_index += 1
#                 rotating_index += 1

#     return array

# print(delete_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 5, 6]))




# def remove_duplicates(array):

#     if not array:
#         return []

#     unique_items = [array[0]]
#     print(unique_items[-1])
#     for item in array:
#         if item != unique_items[-1]:

#             unique_items.append(item)
#     return unique_items


# array = [2,2,2,5,5,4,3,6,4,9]
# without_duplicates = remove_duplicates(sorted(array))

# print(without_duplicates)

class Node:
    def __init__(self, data):
        self.data = data 
        self.ref = None
node = Node(10)
print(node)


# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def print_LL(self):
#         if self.head is None:
#             print('linked list is empty')
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n = n.ref

# LL1 = LinkedList()
# LL1.print_LL()







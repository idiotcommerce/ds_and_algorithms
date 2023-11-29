
# linked list practice

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_LL(self):
        # if self.head is None:
        #     print("this is an empty linked list")
        # else:
        #     n = self.head
        #     while n is not None:
        #         print(n.data, "---->", end = " ")
        #         n = n.ref
        n = self.head
        while n is not None:
            print(n.data, "---->", end = " ")
            n = n.ref


    def add_at_bigin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def add_at_middle(self, data, existed_value):
        new_node = Node(data)
        if self.head is None:
            print("given value not present in the linked list")
        else:
            n = self.head
            while n is not None:
                if n.data == existed_value:
                    new_node.ref = n.ref
                    n.ref = new_node
                    break
                n = n.ref
            else:
                print(" value not presented in linked list ")

    def add_to_empty_linked_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            print('this is not empty linked list')


    def delete_at_begin(self):
        if self.head is None:
            print("empty linked list ")
        else:
            self.head = self.head.ref
    
    def delete_at_end(self):
        if self.head is None:
            print(" empty linked list present ")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_at_middle(self, existed_value):
        if self.head is None:
            print(' empty linked list to delete')
        
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == existed_value:
                    n.ref = n.ref.ref
                    break
                n = n.ref
            else:
                print("data not present ")


LL1 = LinkedList()
LL1.add_at_bigin(20)
LL1.add_at_bigin(10)
LL1.add_at_end(30)
LL1.add_at_end(50)
LL1.add_at_middle(40, 30)
# LL1.delete_at_begin()
# LL1.delete_at_end()
LL1.delete_at_middle(50)

LL1.print_LL()











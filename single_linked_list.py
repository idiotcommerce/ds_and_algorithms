

class Node:
    def __init__(self, data):
        self.data = data 
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print(' this is empty linked list')
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end= " ")
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_ending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_node_after(self, data, present_value):
        new_node = Node(data)
        n = self.head
        while n is not None:
            if n.data == present_value:
                # below 2 lines actually i take temp variable and assign. below is better way
                new_node.ref = n.ref
                n.ref = new_node
                break
            n = n.ref
        else :
            print('data not present in the linked list')


    def add_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print( "linked list is not empty")
            
    def delete_at_begin(self):
        if self.head is None:
            return "linked list is empty"
        elif self.head.ref is None:
            self.head = None

        else:
            self.head = self.head.ref

    def delete_at_end(self):
        if self.head is None:
            return "linked list is empty"
        elif self.head.ref is None:
            self.head = None
            
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_at_middle(self, check):
        if self.head is None:
            return "this is empty linked list"
        else: 
            n = self.head
            while n.ref is not None:
                if n.ref.data == check:
                    n.ref = n.ref.ref
                    break
                n = n.ref
                    

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_ending(35)
LL1.add_begin(25)
LL1.add_ending(55)
LL1.add_node_after(888, 35)

#LL1.delete_at_begin()
#LL1.add_empty(10)
#LL1.delete_at_end()

LL1.delete_at_middle(55)

LL1.print_LL()






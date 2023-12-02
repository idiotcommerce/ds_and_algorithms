
# double linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.pre_ref = None
        self.next_ref = None

class doubleLL:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("this is empty linked list")
        else:
            head = self.head
            while head is not None:
                print(head.data, "====>", end= ' ')
                head = head.next_ref

            
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("linked list is empty")
        else:
            head = self.head
            while head.next_ref is not None:
                head = head.next_ref
            
            while head is not None: # present node data we are checking
                print(head.data, ' <====', end = ' ')
                head = head.pre_ref

    def insert_at_empty_LL(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node

        else:
            print(' linked list is not empty')
    
    def add_at_begin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next_ref = self.head
            self.head.pre_ref = new_node
            self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next_ref is not None:
                n = n.next_ref
            n.next_ref = new_node
            new_node.pre_ref = n
    
    def add_at_after_partiuclar_node(self, data, existed_value):
        
        if self.head is None:
            print(' linked list is empty, so, we can not add the data')
        else:
            head = self.head
            new_node = Node(data)
            while head is not None:
                if head.data == existed_value:
                    new_node.next_ref = head.next_ref
                    new_node.pre_ref = head
                    if head.next_ref is not None:
                        head.next_ref.pre_ref = new_node
                    head.next_ref = new_node
                    break
                head = head.next_ref
            else:
                print('data not present in the linked list')


    def add_at_before_partiuclar_node(self, data, existed_value):
        
        if self.head is None:
            print(' linked list is empty, so, we can not add the data')
        else:
            head = self.head
            new_node = Node(data)
            while head is not None:
                if head.data == existed_value:
                    new_node.pre_ref = head.pre_ref
                    new_node.next_ref = head
                    if head.pre_ref is not None:
                        head.pre_ref.next_ref = new_node
                    else:
                        self.head = new_node
                    head.pre_ref = new_node
                    break
                    
                head = head.next_ref

    def delete_at_begin(self):
        if self.head is None:
            print(' linked list is empty, so we can not delete')
        elif self.head.next_ref is None:
            self.head = None
        else:
            self.head = self.head.next_ref
            self.head.pre_ref = None

    def delete_at_end(self):
        if self.head is None:
            print(' linked list is empty, so we can not delete')
        elif self.head.next_ref is None:
            self.head = None
        else:
            head = self.head
            while head.next_ref is not None:
                head = head.next_ref
            head.pre_ref.next_ref = None

    def delete_at_anywhere(self, deleting_value):
        if self.head is None:
            return 'linked list is empty, we can not delete '
        if self.head.next_ref is None:
            if self.head.data == deleting_value:
                self.head = None
            else:
                return ' given data not present in the linked list'
        if self.head.data == deleting_value:
            self.head = self.head.next_ref
            self.head.pre_ref = None
            
        else:
            head = self.head
            while head.next_ref is not None:
                if head.data == deleting_value:
                    head.pre_ref.next_ref = head.next_ref
                    head.next_ref.pre_ref = head.pre_ref
                    break
                head = head.next_ref
            
            else:
                
                if head.data == deleting_value:
                    head.pre_ref.next_ref = None
                else:
                    print(' data given is not in the linked list ')




            

dll = doubleLL()

dll.insert_at_empty_LL(20)

dll.add_at_begin(10)
dll.add_at_end(40)
dll.add_at_after_partiuclar_node(30, 20)
dll.add_at_after_partiuclar_node(50, 40)
#dll.add_at_after_partiuclar_node(90, 100)

dll.add_at_before_partiuclar_node(45, 50)
dll.add_at_before_partiuclar_node(5, 10)

# dll.delete_at_begin()
#dll.delete_at_end()
dll.delete_at_anywhere(50)

dll.print_LL()
dll.print_LL_reverse()













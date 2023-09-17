class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def apnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pops(self):
        temp = self.head
        if self.length == 0:
            return None
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0 :
            self.head = None
            self.tail = None
            
    def print_lists(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        
mylist = LinkedList(1)
mylist.apnd('3434')
mylist.apnd('786')
mylist.pops()
mylist.print_lists()
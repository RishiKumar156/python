class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def pop(self):
        temp = self.head 
        pre = temp
        if self.length == 0:
            return None
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
    def pop_first(self):
        if self.length == 0:
            self.tail = None
            return None
        temp = self.head 
        self.head = self.head.next 
        temp.next = None
        self.length -= 1
        if self.head is None:
            self.tail = None
            
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        
    def print_nodes(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
test = LinkedList(1)
test.append(2)
test.append(3)
test.append(4)
test.prepend(0)
test.pop()
test.pop_first()
test.print_nodes()
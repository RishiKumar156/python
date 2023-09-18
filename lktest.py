class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
    
class LinkedList():
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
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
        
    def prepend(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        
    def pop_first(self):
        if self.length is None:
            return False
        self.head.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
    
    def print_nodes(self):
        temp = self.head 
        while temp:
            print(temp.value)
            temp = temp.next 
    
    
test = LinkedList(1)
test.append(2)
test.append(3)
test.append(4)
test.pop_first()
test.pop()
test.print_nodes()
class Node():
    def __init__(self,data):
        self.value = data 
        self.next = None 
        self.prev = None 
    

class DoublyLinkedList():
    def __init__(self,data):
        create_node = Node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
    
    
    def append_node(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
            self.tial = create_node
        else:
            self.tail.next = create_node
            create_node.prev = self.tail
            self.tail = create_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None 
            self.tail = None 
        else:
            self.tail = self.tail.prev 
            self.tial.next = None 
            temp.prev = None 
        self.length -= 1
        return temp
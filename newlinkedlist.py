class Node():
    def __init__(self , data):
        self.data = data 
        self.pointer = None
    
class LinkedList():
    def __init__(self, data):
        create_node = Node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
        
    def print_nodes(self):
        t = self.head 
        while t:
            print(t.data)
            t = t.pointer
    
    def prepend(self , data):
        create_node = Node(data)
        if self.head is None:
            self.head = create_node
            self.tail = create_node
        create_node.pointer = self.head
        self.head = create_node
        self.length += 1
        return True

    
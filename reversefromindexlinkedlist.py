class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.pointer = None 
    
    
class LinkedList():
    def __init__(self, data) -> None:
        create_node = Node(data)
        self.head = create_node
        self.length = 1
    
    def append(self,data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
        else:
            tt = self.head 
            while tt.pointer:
                tt = tt.pointer
            tt.pointer = create_node
        self.length += 1
        return create_node
    
    def print_nodes(self):
        return True
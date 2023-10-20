class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.pointer = None 
    
class linkedList():
    def __init__(self,data) -> None:
        create_node = Node(data)
        self.head = create_node
        self.length = 1
    
    
    def append(self, data):
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
        tt = self.head 
        while tt:
            print(tt.data)
            tt = tt.pointer
    
    def reverson_index(self, start_index, end_index):
        dummy = Node(0)
        dummy.pointer = self.head 
        prev = dummy
        
        for _ in range(start_index):
            prev = prev.pointer 
        current_node = prev.pointer
        for _ in range(end_index-start_index):
            next_node = current_node.pointer 
            current_node.pointer = next_node.pointer 
            next_node.pointer = prev.pointer 
            prev.pointer = next_node
        
        self.head = dummy.pointer 
    
mynode = linkedList(1)
mynode.append(2)
mynode.append(3)
mynode.append(4)
mynode.append(5)
mynode.reverson_index(2,3)
mynode.print_nodes()
        
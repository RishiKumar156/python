class Node():
    def __init__(self,data) -> None:
        self.value = data 
        self.next = None 

class LinkedList():
    def __init__(self,data) -> None:
        create_node = Node(data)
        self.head = create_node
        self.length = 1
    
    def append_nodeS(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
        else:
            tt = self.head 
            while tt.next:
                tt = tt.next 
        tt.next = create_node
        self.length += 1
    
    def print_nodes(self):
        tt = self.head 
        while tt:
            print(tt.value)
            tt = tt.next 
    
    def rever_between(self, start_index , end_index):
        dummy = Node(0)
        dummy.next = self.head 
        prev = dummy 
        
        for _ in range(start_index):
            prev = prev.next 
        current_node = prev.next 
        for _ in range(end_index-start_index):
            next_node = current_node.next 
            current_node.next = next_node.next 
            next_node.next = prev.next 
            prev.next  = next_node 
        self.head = dummy.next 
    
mynode = LinkedList(1)
mynode.append_nodeS(2)
mynode.append_nodeS(3)
mynode.append_nodeS(4)
mynode.append_nodeS(5)
mynode.rever_between(2,3)
mynode.print_nodes()
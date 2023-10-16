class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.pointer = None 
        
    
class LinkedList():
    def __init__(self, data) -> None:
        cnode = Node(data)
        self.head = cnode
        self.tail = cnode
        self.length = 1 
    
    def append(self, data):
        cnode = Node(data)
        if not self.head:
            self.head  = cnode
            self.tail = cnode
        else:
            self.tail.pointer = cnode
            self.tail = cnode
        self.length += 1 
        return cnode
    
    def partition_list(self, k):
        lesser_head = None 
        lesser_tail = None 
        greater_head = None 
        greater_tail = None 
        tt = self.head 
        while tt:
            next_node  = tt.pointer 
            tt.pointer = None 
            if tt.data < k:
                if not lesser_head:
                    lesser_head = tt
                    lesser_tail = tt 
                else:
                    lesser_tail.pointer = tt 
                    lesser_tail = tt 
            if tt.data > k:
                if not greater_head:
                    greater_head = tt 
                    greater_tail = tt 
                else:
                    greater_tail.pointer = tt
                    greater_tail = tt 
            tt = next_node 
        if not lesser_head:
            new_node = greater_head
        else:
            lesser_tail.pointer = greater_head
            new_node = lesser_head
        return new_node
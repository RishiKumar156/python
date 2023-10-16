class Node():
    def __init__(self, data) -> None:
        self.data = data 
        self.pointer = None 
    
class LinkedList():
    def __init__(self,data) -> None:
        cnode = Node(data)
        self.head = cnode
        self.tail = cnode
        self.length = 1
        
    def print_nodes(self):
        tt = self.head 
        while tt:
            print(tt.data)
            tt = tt.pointer
        
    def add_node(self, data):
        cnode = Node(data)
        if not self.head:
            self.head = cnode
            self.tail = cnode
        else:
            self.tail.pointer = cnode
            self.tail = cnode
        self.length += 1
        return cnode.data
    
    def prepend(self, data):
        cnode = Node(data)
        if not self.head:
            self.head = cnode
            self.tail = cnode
        else:
            cnode.pointer = self.head
            self.head = cnode
        self.length += 1
        return cnode
    
    def pop(self):
        if self.length == 0:
            return None
        tt = self.head 
        prev = tt 
        while tt.pointer:
            prev = tt 
            tt = tt.pointer
        self.tail = prev
        self.tail.pointer = None 
        self.length -= 1
        if self.length == 0:
            self.head = None 
            self.tail = None 
        return tt.data
    
    def pop_first(self):
        temp = self.head 
        self.head = self.head.pointer 
        temp.pointer = None 
        if not self.head:
            return None 
        self.length -= 1
        if self.length == 0:
            self.tail = None 
        return temp.data
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        tt = self.head 
        for _ in range(index):
            tt= tt.pointer
        return tt
    
    def set(self, data, index):
        if index < 0 or index > self.length:
            return None 
        t = self.get(index)
        t.data = data 
        return t
    
    def insert(self, index, data):
        if index < 0 or index >= self.length:
            return None 
        if index == self.length:
            return self.add_node(data)
        if index == 0:
            return self.prepend(data)
        prev = self.get(index -1)
        cnode = Node(data)
        cnode.pointer = prev.pointer
        prev.pointer = cnode.pointer
        self.length += 1
        return cnode
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        
        prev = self.get(index-1)
        cnode = prev.pointer 
        prev.pointer = cnode.pointer 
        cnode.pointer = None 
        self.length -= 1
        return cnode
    
    def reverse(self):
        tt = self.head 
        self.head = self.tail 
        self.tail = tt 
        before = None 
        for _ in range(self.length):
            after = tt.pointer 
            tt.pointer = before 
            before = tt 
            tt = after 
        return tt
    
    
    def reversenodeofkth(self, k):
        if k < 0 or k >= self.length:
            return None 
        slower_node = self.head 
        faster_node = self.head 
        
        for _ in range(k):
            if not faster_node:
                return None
            faster_node = faster_node.pointer
            
        while faster_node:
            slower_node = slower_node.pointer
            faster_node = faster_node.pointer
        k = print(slower_node.data)
        return k 


mynode = LinkedList(1)
mynode.add_node(2)
mynode.add_node(3)
mynode.add_node(4)
mynode.reversenodeofkth(1)
# mynode.print_nodes()
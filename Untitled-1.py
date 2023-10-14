class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.pointer = None
        
class LinkedList():
    def __init__(self, data) -> None:
        cn = Node(data)
        self.head = cn 
        self.tail = cn 
        self.length = 1
    
    def print_nodes(self):
        ttnodes = self.head
        while ttnodes:
            print(ttnodes.data)
            ttnodes = ttnodes.pointer 
    
    def prepend(self, data):
        cn = Node(data)
        if not self.head:
            self.head = cn 
            self.tail = cn 
        else:
            cn.pointer = self.head
            self.head = cn 
        self.length += 1
        return cn 
    
    def append_node(self, data):
        cn = Node(data)
        if not self.head:
            self.head = cn 
            self.tail = cn 
        else:
            self.tail.pointer = cn
            self.tail = cn
        self.length += 1
        return cn 
    
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        tnode = self.head
        for _ in range(index):
            tnode = tnode.pointer
        return tnode
    
    def set_node(self, index, data):
        node = self.get_node(index)
        if node:
            node.data = data
        return node
    
    def pop_node(self):
        if self.length <= 0:
            return None
        ttnodes = self.head
        previous_node = None
        while ttnodes.pointer:
            previous_node = ttnodes
            ttnodes = ttnodes.pointer
        if previous_node:
            previous_node.pointer = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return ttnodes
    
    def pop_first_node(self):
        if self.length <= 0:
            return None
        tt_nodes = self.head
        self.head = tt_nodes.pointer
        if self.length == 1:
            self.tail = None
        self.length -= 1
        return tt_nodes
    
    def insert_node(self, index, data):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append_node(data)
        
        crnode = Node(data)
        prev_node = self.get_node(index - 1)
        crnode.pointer = prev_node.pointer
        prev_node.pointer = crnode
        self.length += 1 
        return crnode

mynode = LinkedList(897)
mynode.append_node(7898)
print(f'Removed node is {mynode.pop_node().data}')

class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.pointer = None
    
class LinkedList():
    def __init__(self, data):
        cn = Node(data)
        self.head = cn 
        self.tail = cn 
        self.length = 0 
    
    def print_nodes(self):
        nodes = self.head
        while nodes:
            print(nodes.data)
            nodes = nodes.pointer
        
    def ppa(self, data):
        cn = Node(data)
        if not self.head:
            self.head = cn 
            self.tail = cn 
        else:
            cn.pointer = self.head
            self.head = cn 
        self.length += 1
    
    def add_node(self, data):
        cn = Node(data)
        if not self.head:
            self.head = cn 
            self.tail = cn 
        else:
            ttnodes = self.head
            while ttnodes.pointer:
                ttnodes = ttnodes.pointer
            ttnodes.pointer = cn 
        self.length += 1
        return cn 
    
    def get_node(self , index):
        if index < 0 or index >= self.length:
            return None 
        else:
            crntNode = self.head
            for _ in range(index):
                crntNode = crntNode.pointer
            return crntNode
    
    def set_node(self , data , index):
        if index < 0 or index >= self.length :
            return None
        get_node = self.get_node(index)
        get_node.pointer = data
        return get_node
    
    def ppf(self):
        if self.length <= 0:
            return None 
        else:
            nodes = self.head
            self.head.pointer = nodes
            nodes.pointer = None 
            self.length -= 1
        return nodes
    
    def pp(self):
        if self.length == 0:
            self.head = None 
            self.tail = None
            return None 
        else:
            crntnode = self.head
            prev = crntnode
            while crntnode.pointer:
                prev = crntnode
                crntnode = crntnode.pointer
            self.tail = prev
            self.tail.pointer = None 
            self.length -= 1
        return crntnode
    
    def insert_node(self, data , index):
        if self.length == 0:
            return self.ppa(data)
        if index < 0 or index > self.length:
            return None
        if self.length == 1:
            return self.add_node(data)
        new_node = Node(data)
        get_prev = self.get_node(index - 1)
        new_node.pointer = get_prev.pointer
        get_prev.pointer = new_node
        self.length += 1
        return new_node
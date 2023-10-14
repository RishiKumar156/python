class Node():
    def __init__(self, data):
        self.data = data
        self.pointer = None

class Listlinked():
    def __init__(self, data):
        create_node = Node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
    
    def prepend_node(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
            self.tail = create_node
        else:
            create_node.pointer = self.head
            self.head = create_node
        self.length += 1
        return create_node
    
    def append_node(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
            self.tail = create_node
        else:
            temp = self.head 
            while temp.pointer:
                temp = temp.pointer 
            temp.pointer = create_node
        self.length += 1
        return create_node
    
    def append_begining(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
            self.tail = create_node
        else:
            create_node.pointer = self.head 
            self.head = create_node 
        self.length += 1
        return create_node
    
    def set_node (self, index , data):
        if index < 0 or index >= self.length:
            return None 
        else:
            find = self.get_nodes(index)
            find.data = data 
        return find
    
    def get_nodes(self, index):
        if index < 0 or index >= self.length:
            return None 
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.pointer
        return temp
    
    def delete_node(self):
        ttnodes = self.head 
        prev_node = ttnodes
        while ttnodes.pointer:
            prev_node = ttnodes
            ttnodes = ttnodes.pointer 
        self.tail = prev_node
        self.tail.pointer = None 
        self.length -= 1
        return ttnodes
    
    def delete_first_node(self):
        if self.length == 0:
            return None 
        else:
            allnodes = self.head 
            self.head.pointer = allnodes.pointer
            allnodes.pointer = None 
        self.length -= 1
        
    def insert_node(self, index, data):
        create_node = Node(data)
        if index < 0:
            return None
        if index == 0:
            return self.append_begining(data)
        if index == self.length:
            return self.append_node(data)
        prev_node = self.get_nodes(index - 1)
        create_node.pointer = prev_node.pointer
        prev_node.pointer = create_node
        self.length += 1
        return create_node
    
    def remove_node(self, index):
        if index == 0:return self.delete_first_node()
        if index <0: return None 
        if index == self.length : return self.delete_node()
        prevnpde = self.get_nodes(index-1)
        nextnode = prevnpde.pointer
        prevnpde.pointer = nextnode.pointer
        nextnode.pointer = None 
        self.length -= 1
        return nextnode        
    
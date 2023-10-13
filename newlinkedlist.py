

class Node():
    def __init__(self, data):
        self.data = data
        self.pointer = None
    
class LinkedList():
    def __init__(self,data):
        cn = Node(data)
        self.head = cn 
        self.tail = cn
        self.length = 1
    
    def print_node(self):
        node_item = self.head 
        while node_item :
            print(node_item.data)
            node_item = node_item.pointer
        
    def prepend_node(self , data):
        cn = Node(data)
        if self.head is None:
            self.head = cn 
            self.tail = cn 
        else:
            cn.pointer = self.head
            self.head = cn 
        self.length += 1
    
    def add_node(self, data):
        cn = Node(data)
        if self.head is None:
            self.head = cn 
            self.tail = cn 
        else :
            self.tail.pointer = cn 
            self.tail = cn 
        self.length += 1
    
    def pp(self):
        if self.length == 0:
            return None
        ct = self.head
        pvt = ct
        while ct.pointer is not None:
            pvt = ct 
            ct = ct.pointer
        self.tail = pvt
        self.tail.pointer = None
        self.length -= 1
        return True
    
    def ppf(self):
        if self.length == 0:
            return None
        ct = self.head
        self.head = self.head.pointer
        ct.pointer = None
        self.length -= 1
        return ct.data
    
    def get_node(self , index):
        if index < 0 or index >= self.length:
            return None
        ct = self.head
        for _ in range(index):
            ct = ct.pointer
        return ct

    def set_node_data(self, index , data):
        if index < 0 or index >= self.length:
            return None
        ct = self.get_node(index)
        ct.data = data
        return ct
    
    def insert_data(self , index , data):
        if index < 0 or index >= self.length :
            return None
        if index == 0:
            return self.prepend_node(data)
        if index == self.length:
            return self.add_node(data)
        cn = Node(data)
        find_node = self.get_node(index-1)
        cn.pointer = find_node.pointer
        find_node.pointer = cn
        self.length += 1
        return True
    
mynode = LinkedList(678)
mynode.add_node(90)
mynode.prepend_node(786)
mynode.insert_data(1 , 567)
print(f'Pop first node is {mynode.ppf()}')
mynode.print_node()
# print(f'Get node is index {mynode.set_node_data(0, 786)}')
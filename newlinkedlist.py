class nodes():
    def __init__(self, data):
        self.data = data
        self.pointer = None
        

class LinkedList():
    def __init__(self , data):
        c_node = nodes(data)
        self.head = c_node
        self.tail = c_node
        self.length = 1
        
    def create_node(self,data):
        c_node = nodes(data)
        if self.head is None:
            self.head = c_node
            self.tail = c_node
        else:
            self.tail.pointer = c_node
        self.length += 1
        return True
    
    def print_list(self):
        curn_node = self.head
        while curn_node is not None:
            print(curn_node.data)
            curn_node = curn_node.pointer
    
    def pp(self):
        if self.length == 0:
            return 0
        c_n = self.head
        pv_n = self.head
        while c_n.pointer is not None:
            pv_n = c_n
            c_n = c_n.pointer
        self.tail = pv_n
        self.tail.pointer = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        k = print(c_n.data)
        return k
    
mynode = LinkedList(345)
mynode.create_node(786)
mynode.pp()
mynode.print_list()
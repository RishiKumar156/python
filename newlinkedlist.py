class node():
    def __init__(self , data):
        self.data = data 
        self.pointer = None 
        
    
class LinkedList():
    def __init__(self , data):
        create_node = node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
    
    def print_nodes(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.pointer
        
    def add_node(self, data):
        create_node = node(data)
        if self.head is None:
            self.head = create_node
            self.tail = create_node
        else :
            self.tail.pointer = create_node
            self.tail = create_node
        self.length += 1
    
    def prepend_node(self, data):
        create_node = node(data)
        if self.head is None:
            self.head = create_node
            self.tail = create_node
        else:
            create_node.pointer = self.head
            self.head = create_node
        self.length += 1
        return True
    
    def pp(self):
        if self.length == 0:
            return 0
        ct = self.head
        pvt = ct
        while ct.pointer is not None:
            pvt = ct 
            ct = ct.pointer
        self.tail = pvt
        self.tail.pointer = None
        self.length -= 1
        k = print(f'Poped item {ct.data}')
        return k
    
    def ppf(self):
        if self.length == 0:
            return 0 
        first_item = self.head 
        self.head = self.head.pointer
        first_item.pointer = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        k = print(f'First node deleted {first_item.data}')
        return k 
        
    def get_node(self , index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.pointer
        return temp.data

mynode = LinkedList(908)
# mynode.get_node(0)
print(f'The found node is {mynode.get_node(0)}')
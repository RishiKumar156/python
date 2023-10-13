class Node():
    def __init__(self , data):
        self.data = data 
        self.pointer = None
    
class LinkedList():
    def __init__(self, data):
        create_node = Node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
        
    def print_nodes(self):
        t = self.head 
        while t:
            print(t.data)
            t = t.pointer
    
    def prepend(self , data):
        create_node = Node(data)
        if self.head is None:
            self.head = create_node
            self.tail = create_node
        create_node.pointer = self.head
        self.head = create_node
        self.length += 1
        return True

    def add_node(self , data):
        create_node = Node(data)
        if self.length == 0 or self.head is None:
            self.head = create_node
            self.tail = create_node
        total_nodes = self.head
        while total_nodes.pointer is not None:
            total_nodes = total_nodes.pointer
        total_nodes.pointer = create_node
        self.length+= 1
        return True
    
    def get_node(self , index):
        if index < 0 or index >= self.length:
            return None
        total_nodes = self.head
        for _ in range(index):
            total_nodes = total_nodes.pointer
        return total_nodes
    
    def set_nodes_data(self, index, data):
        if index < 0 or index >= self.length:
            find = self.get_node(index)
            find.data = data
        return find
    
    def pp(self):
        if self.length < 0:
            return None
        total_nodes = self.head 
        previous_nodes = total_nodes
        while total_nodes.pointer is not None:
            previous_nodes = total_nodes
            total_nodes  = total_nodes.pointer
        self.tail = previous_nodes
        self.tail.pointer = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return total_nodes
    
    def ppf(self):
        if self.length < 0:
            return None
        first_item = self.head
        self.head = self.head.pointer
        first_item.pointer = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return first_item

    def insert_node(self , index , data):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.add_node(data)
        create_node = Node(data)
        find_prev = self.get_node(index -1)
        create_node.pointer = find_prev.pointer
        find_prev.pointer = create_node
        self.length += 1
        return create_node
    
    def remove_node(self , index):
        if index < 0 or index > self.length:
            return None
        if self.length == index :
            return self.pp()
        if self.length == 0:
            return self.ppf()
        prev = self.get_node(index-1)
        prev.pointer = None 
        next = self.get_node(index+1)
        prev.pointer = next
        return True
                
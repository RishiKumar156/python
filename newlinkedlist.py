class Nodes():
    def __init__(self, data):
        self.data = data 
        self.pointer = None

class LinkedList():
    def __init__(self, data):
        create_node = Nodes(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
    
    def print_nodes(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.pointer
    
    def add_node_at_first(self, data):
        create_node = Nodes(data)
        if self.head is None:
            self.head = create_node
            self.tail = create_node
        else:
            create_node.pointer = self.head
            self.head = create_node
        self.length += 1
        return create_node
    
    def add_node(self , data):
        create_node = Nodes(data)
        if self.head is None:
            self.head = create_node
            self.tail = create_node
        else:
            total_nodes = self.head
            while total_nodes.pointer is not None:
                total_nodes = total_nodes.pointer
            total_nodes.pointer = create_node
            self.length += 1
        return create_node
    
    def get_nodes(self , index):
        if index < 0 or index >= self.length:
            return None
        total_nodes = self.head
        for _ in range(index):
            total_nodes = total_nodes.pointer
        return total_nodes
    
    def set_nodes_data(self, data, index):
        if index < 0 or index >= self.length:
            return None
        findnode = self.get_nodes(index)
        findnode.data = data
        return findnode

    def pp(self):
        if self.length == 0:
            return None
        total_nodes = self.head
        previous_node = total_nodes
        while total_nodes.pointer is not None:
            previous_node = total_nodes
            total_nodes = total_nodes.pointer
        self.tail = previous_node
        self.tail.pointer = None
        self.length -= 1
        return total_nodes
    
    def ppf(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        first_node = self.head
        self.head = first_node.pointer
        first_node.pointer = None 
        self.length -= 1
        return first_node
    
    def insert_node(self , index , data):
        create_node = Nodes(data)
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return self.add_node_at_first(data)
        if index == self.length:
            return self.add_node(data)
        previous_node = self.get_nodes(index-1)
        create_node.pointer = previous_node.pointer
        previous_node.pointer = create_node
        self.length += 1
        return create_node
    
    def remove_node(self, index):
        if index == 0:
            return self.ppf()
        if index == self.length:
            return self.pp()
        if index < 0:
            return None
        if index == 1 and self.length == 1:
            self.head = None
            self.tail = None
        previous_node = self.get_nodes(index-1)
        given_node = previous_node.pointer
        previous_node.pointer = given_node.pointer
        self.length -= 1
        return after_node
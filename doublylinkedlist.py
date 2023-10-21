class Node():
    def __init__(self,data):
        self.value = data 
        self.next = None 
        self.prev = None 
    

class DoublyLinkedList():
    def __init__(self,data):
        create_node = Node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
    
    def print_nodes(self):
        temp = self.head 
        while temp:
            print(temp.value)
            temp = temp.next 
            
    def append_node(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
            self.tial = create_node
        else:
            self.tail.next = create_node
            create_node.prev = self.tail
            self.tail = create_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None 
            self.tail = None 
            return None
        else:
            self.tail = self.tail.prev 
            self.tail.next = None 
            temp.prev = None 
        self.length -= 1
        return temp
    
    def prepend(self,data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
            self.tail = create_node
        create_node.next = self.head 
        self.head.prev = create_node
        self.head = create_node
        self.length += 1
        return create_node
    
    def pop_first(self):
        first_node = self.head 
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None 
            self.tail = None 
        else:
            self.head = self.head.next 
            self.head.prev = None 
            first_node.next = None 
        self.length -= 1
        k = print(first_node.value)
        return k
    def get(self, index):
        if index > self.length:
            return None 
        tt = self.head 
        for _ in range(index):
            tt = tt.next
        return tt
    def remove(self, index):
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        if index < 0 or index >= self.length - 1:
            return None 
        temp = self.get(index)
        temp.next.prev = temp.prev 
        temp.prev.next  = temp.next
        temp.next = None 
        temp.prev = None
        self.length -= 1
        return temp
mynode = DoublyLinkedList(8)
mynode.append_node(6)
mynode.append_node(3)
mynode.prepend(7)
mynode.pop()
mynode.pop_first()
mynode.print_nodes()
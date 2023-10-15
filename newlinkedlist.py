class Node():
    def __init__(self,data):
        self.data = data 
        self.pointer = None 
    
class LinkedList():
    def __init__(self, data):
        create_node = Node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
    
    def print_nodes(self):
        temp = self.head 
        while temp:
            print(temp.data)
            temp = temp.pointer 
    
    def append(self , data):
        create_node = Node(data)
        if self.length < 0:
            self.head = create_node
            self.tail = create_node
        self.tail.pointer = create_node
        self.tail = create_node
        self.length += 1
        return create_node
    
    def prepend(self, data):
        create_node = Node(data)
        if self.length < 0 :
            self.head = create_node
            self.tail = create_node
        create_node.pointer = self.head 
        self.head = create_node
        self.length += 1
        return create_node
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        items = self.head 
        for _ in range(index):
            items = items.pointer
        return items
    
    def set(self, index, data):
        if index < 0 or index >= self.length:
            return None 
        temp = self.get(index)
        temp.data = data
        return temp
    
    def pop(self):
        items = self.head 
        if self.length <= 0 :
            return None 
        temp = self.head 
        prev = temp
        while temp.pointer:
            prev = temp
            temp = temp.pointer
        self.tail = prev
        self.tail.pointer = None 
        self.length -= 1
        if self.length == 0:
            self.tail = None 
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None 
        temp = self.head 
        self.head = self.head.pointer
        temp.pointer = None 
        self.length -= 1
        if self.length <= 0:
            self.head = None 
            self.tail = None 
        return temp
    
    def insert(self, index , data):
        create_node = Node(data)
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append(data)
        if index < 0 or index >= self.length:
            return None 
        prev = self.get(index -1)
        create_node.pointer = prev.pointer
        prev.pointer = create_node
        self.length += 1
        return create_node
    
    def remove(self, index):
        if index == 0: return self.pop_first()
        if index == self.length : return self.pop()
        if index < 0 or index >= self.length: return None 
        prev = self.get(index -1)
        temp = prev.pointer
        prev.pointer = temp.pointer 
        temp.pointer = None 
        self.length -=1 
        return temp 
    
    def reverse(self):
        temp = self.head 
        self.head = self.tail 
        self.tail = temp 
        before = None  
        for _ in range(self.length):
            after = temp.pointer #keep the track of current item 
            temp.pointer = before # choosing the value 
            before = temp # changing in to None 
            temp = after  # using the track moving on for next item 
        return temp 
    
mynode = LinkedList(1)
mynode.append(2)
mynode.append(3)
mynode.append(4)
mynode.reverse()
mynode.print_nodes()
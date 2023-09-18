class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def pop(self):
        temp = self.head 
        pre = temp
        if self.length == 0:
            return None
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        
    def pop_first(self):
        if self.length == 0:
            self.tail = None
            return None
        temp = self.head 
        self.head = self.head.next 
        temp.next = None
        self.length -= 1
        if self.head is None:
            self.tail = None
            
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        
    def Get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head 
        lent = 0 
        while temp:
            if (lent == index):
                print(f'Index entered is {index} & value is {temp.value}')
            temp = temp.next
            lent+=1
    def set_value(self,index ,value):
        temp = self.head 
        lnt = 0 
        while temp:
            if lnt == index:
                temp.value = value
                print(f'Index entered is {index} & Updated value is {temp.value}')
            temp = temp.next
            lnt += 1
    def print_nodes(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            
test = LinkedList(0)
test.append(1)
test.append(2)
test.append(8)
test.append(4)


# test.pop()
# test.pop_first()
# test.print_nodes()
test.Get(0)
test.set_value(0,10)
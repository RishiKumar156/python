class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def pop(self):
        if self.head is None :
            return None
        temp = self.head
        while temp:
            pre = temp 
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        
    def print_lists(self):
        temp = self.head 
        while temp:
            print(temp.value)
            temp = temp.next
    
mylist = LinkedList(1)
# mylist.pop_first()
mylist.append('2')
mylist.append('3')
mylist.append('4')
# mylist.pop_first()
mylist.print_lists()
class Node:
    def __init__(self,data) -> None:
        self.value = data
        self.next = None
    
class Queue:
    def __init__(self,data) -> None:
        create_node = Node(data)
        self.first = create_node
        self.last = create_node
        self.length = 1
    
    def print_nodes(self):
        while self.first:
            print(self.first.value)
            self.first = self.first.next
    
    def enqueue (self, data):
        create_node = Node(data)
        if not self.first:
            self.first = create_node
        else:
            self.last.next = create_node
            self.last = create_node
        self.length += 1
        return create_node
    
    def dequeue (self):
        if self.length == 0:
            return None 
        else:
            temp = self.first
            self.first = self.first.next 
            temp.next = None 
            self.length -=1 
            if self.length == 0:
                self.first = None 
                self.tail = None 
            k = print(f'Remove value is {temp.value}')
        return k
myqueue = Queue(3)
myqueue.enqueue(4)
myqueue.dequeue()
myqueue.print_nodes()
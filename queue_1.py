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
        temp = self.first
        if self.length == 1:
            self.first = None 
            self.last = None 
        else:
            self.first = self.first.next 
            temp.next = None 
            self.length -=1 
        return temp
myqueue = Queue(3)
myqueue.enqueue(4)
print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())
# myqueue.print_nodes()
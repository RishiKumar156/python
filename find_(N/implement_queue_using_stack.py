class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    #Function to push an element into the queue.
    def push(self, item): 
        new_node = Node(item)
        if not self.head:
            self.head = new_node 
            self.tail = new_node 
            return self.head
        else:
            self.tail.next = new_node 
            self.tail = new_node
         #Add code here
    
    #Function to pop front element from the queue.
    def pop(self):
        if not self.head:
            return -1
        data = self.head.data
        self.head = self.head.next
        return data 
        #add code here

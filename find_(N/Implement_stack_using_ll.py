"""Task is to implement stack using linked list"""
class MyStack:

    def __init__(self):
        self.head = None 
    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    #Function to push an integer into the stack.
    def push(self, data):
        new = StackNode(data)
        new.next = self.head 
        self.head = new
        # Add code here
    #Function to remove an item from top of the stack.
    def pop(self):
        if not self.head:
            return -1
        temp = self.head
        self.head = self.head.next 
        return temp.data
        # Add code here

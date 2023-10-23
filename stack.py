class Node:
    def __init__(self,data) -> None:
        self.value = data
        self.next = None 
    
class Stack:
    def __init__(self,data) -> None:
        create_node = Node(data)
        self.top = create_node
        self.height = 1
        
    def print_stack(self):
        temp = self.top 
        while temp:
            print(temp.value)
            temp = temp.next 
    def push(self,data):
        create_node = Node(data)
        if not self.top:
            self.top = create_node
        create_node.next = self.top 
        self.top = create_node
        self.height += 1
        return create_node
    def pop(self):
        if self.height == 0:
            return None 
        temp = self.top 
        self.top = self.top.next 
        temp.next = None 
        self.height -= 1
        if self.height == 0:
            self.top = None 
        k = print(f'Poped item is {temp}')
        return k
        
mystack = Stack(7)
mystack.push(23)
mystack.push(3)
mystack.push(11)
mystack.pop()
mystack.print_stack()
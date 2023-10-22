"""swap first and last value in a linked list"""
class Node:
    def __init__(self,data) -> None:
        self.value = data 
        self.next = None 

class LinkedList:
    def __init__(self,data) -> None:
        create_node = Node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1
    
    def reverse_first_last_nodes_value(self):
        if self.length == 0:
            return None 
        if self.length == 1:
            return None 
        self.head.value , self.tail.value = self.tail.value , self.head.value
        return self.head
    
    def reverse_list_nodes(self):
        current = self.head 
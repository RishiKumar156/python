"""Delete node in singly linked list"""

class Node:
    def __init__(self,value) -> None:
        self.value = value 
        self.next = None 

class LinkedList:
    def __init__(self,value) -> None:
        self.head = Node(value)
    
    def _insert(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head 
            while temp:
                prev = temp
                temp = temp.next
            prev.next = new_node
    
    def pre_pend(self,value):
        new_node = Node(value)
        new_node.next = self.head 
        self.head = new_node
    
    def delete_node(self,head,index):
        temp = head 
        if index == 1:
            temp = temp.next 
            return temp 
        i = 1
        while temp:
            if i == index:
                prev.next = temp.next 
                temp.next = None 
            prev = temp
            temp = temp.next 
            i += 1
        return head 

    def prin_nodes(self):
        nodes = self.head 
        while nodes:
            print(nodes.value, end=" ")
            nodes = nodes.next 

Mynode = LinkedList(1)
Mynode._insert(2)
Mynode._insert(3)
Mynode._insert(4)
Mynode._insert(5)
nodes = Mynode.head
Mynode.delete_node(nodes,4)
Mynode.prin_nodes()
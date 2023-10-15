"""Task is to find the middle one in the linked list we can run on set of list faster 
and another slower , the same linkedlist one set faster and other sloewr 
"""

class Node():
    def __init__(self, data):
        self.data = data 
        self.pointer = None 
    
class LinkedList():
    def __init__(self, data):
        create_node = Node(data)
        self.head = create_node
        self.tail = create_node
        self.length = 1 
        
    def append_nodes(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
            self.tail = create_node
        else:
            self.tail.pointer = create_node
            self.tail = create_node
        self.length += 1
        return create_node
    
    """To find the middle node of a singly linked list without using the length variable, you can use the "two-pointer" or "tortoise and hare" approach. Here's how it works:

Initialize two pointers, one slow (tortoise) and one fast (hare). Start both pointers at the head of the linked list.

Move the fast pointer twice as fast as the slow pointer. For each step, advance the slow pointer one node, and the fast pointer two nodes. This means that the fast pointer covers twice the distance as the slow pointer.

When the fast pointer reaches the end of the list (i.e., the fast pointer becomes None), the slow pointer will be at the middle node of the list. This is because the fast pointer has covered twice the distance, so the slow pointer will be at the halfway point."""

    def find_the_middle(self):
        faster_node = self.head 
        slower_node = self.head 
        if not self.head:
            return None
        while faster_node and faster_node.pointer:
            slower_node = slower_node.pointer
            faster_node = faster_node.pointer.pointer
        return slower_node.data
    

mynode = LinkedList(234)
mynode.append_nodes(222)
mynode.append_nodes(123)
print(f'The middle node is {mynode.find_the_middle()}')
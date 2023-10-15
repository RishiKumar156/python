"""
LL: Has Loop ( ** Interview Question)
Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.

The method should follow these guidelines:



Create two pointers, slow and fast, both initially pointing to the head of the linked list.

Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.

If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False."""

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
    
    def append_node(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
            self.tail = create_node
        else:
            self.tail.pointer = create_node
            self.tail = create_node
        self.length += 1
        return create_node.data
    """Need to follow the same steps for find the middle one in the node onluy change is that
    wether there are same if there are then we are having a loop inside of it"""
    def hash_loop(self):
        if not self.head:
            return False
        faster_node = self.head
        slower_node = self.head 
        while faster_node and faster_node.pointer:
            slower_node = slower_node.pointer
            faster_node = faster_node.pointer.pointer 
            if slower_node == faster_node:
                return True 
        return False

mynode = LinkedList(1)
mynode.append_node(2)
mynode.append_node(3)
mynode.append_node(4)
mynode.append_node(5)
print(f'Return True if loop exists else return False, output is :{mynode.hash_loop()}')
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.pointer = None 
    
    
class LinkedList():
    def __init__(self, data) -> None:
        create_node = Node(data)
        self.head = create_node
        self.length = 1
    
    def append(self,data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
        else:
            tt = self.head 
            while tt.pointer:
                tt = tt.pointer
            tt.pointer = create_node
        self.length += 1
        return create_node
    
    def print_nodes(self):
        if not self.head:
            return None 
        else:
            tt = self.head 
            while tt:
                print(tt.data)
                tt = tt.pointer
        
    def reverse_on_index(self, start, end):
        dummy = Node(0)
        dummy.pointer = self.head
        prev = dummy

        for _ in range(start - 1):
            prev = prev.pointer

        current = prev.pointer
        for _ in range(end - start):
            next_node = current.pointer
            current.pointer = next_node.pointer
            next_node.pointer = prev.pointer
            prev.pointer = next_node

        self.head = dummy.pointer
 
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.reverse_on_index(4 , 5)
linked_list.print_nodes()
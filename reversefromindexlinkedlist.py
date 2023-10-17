class Node():
    def __init__(self, data) -> None:
        self.data = data 
        self.pointer = None 

class LinkedList():
    def __init__(self, data) -> None:
        create_node = Node(data)
        self.head = create_node
        self.length = 1
        
    def append(self, data):
        create_node = Node(data)
        if not self.head:
            self.head = create_node
        else:
            temp = self.head 
            while temp.pointer:
                temp = temp.pointer
            temp.pointer = create_node
        self.length += 1
        
    def print_nodes(self):
        temp = self.head 
        while temp:
            print(temp.data)
            temp = temp.pointer
    
    def reverse_between(self, start , end): 
        first_node = self.head 
        middle_node = None 
        for _ in range(start-1):
            first_node = first_node.pointer
        temp = first_node
        first_node.pointer = None 
        
        middle_node = temp
        for _ in range(start , end-1):
            middle_node = middle_node.pointer
        third_node = middle_node
        middle_node.pointer = None 
        
        prev = None 
        while middle_node.pointer:
            next_node = middle_node.pointer 
            middle_node.pointer = prev 
            prev = middle_node
            middle_node = next_node
        
        last_node_first_set = temp
        while last_node_first_set.pointer:
            last_node_first_set = last_node_first_set.pointer
        last_node_first_set.pointer = prev 
        
        last_node_reversed_middle = prev 
        while last_node_reversed_middle.pointer:
            last_node_reversed_middle = last_node_reversed_middle.pointer
        last_node_reversed_middle.pointer = third_node
        return temp
        
        
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_nodes()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)

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
            while tt.pointer:
                print(tt.data)
                tt = tt.pointer
        return True
    
    def reverse_the_nodes(self, start, end):
        if start < self.length and end > self.length:
            return None 

        node_one = None
        node_two = None
        node_three = None

        current = self.head
        index = 1

        while current:
            if index <= start:
                node_one = current
                print(f'From node one {index}')
            node_one.pointer = None
            while node_one:
                print(node_one.data)
                node_one = node_one.pointer
            
            if index > start and index <= end:
                node_two = current
                print(f'From node two {index, node_two.data}')
            if index > end:
                node_three = current
                print(f'From node three {index, node_three.data}')
            current = current.pointer
            index += 1

# Now you can access node_one, node_two, and node_three outside the loop

        


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.reverse_the_nodes(2, 4)
# linked_list.print_nodes()
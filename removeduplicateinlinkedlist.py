class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.pointer = None 
    
    
class LinkedList():
    def __init__(self,data) -> None:
        create_node = Node(data)
        self.head = create_node
        self.length = 1
        
    def append(self, data):
        create_node = Node(data)
        if not self.head :
            self.head = create_node
        else:
            tt = self.head 
            while tt.pointer:
                tt = tt.pointer
            tt.pointer = create_node
            self.length += 1
        return tt 
    
    def print_nodes(self):
        tt = self.head 
        while tt:
            print(tt.data)
            tt = tt.pointer
    
    def remove_duplicates(self):
        temp = self.head
        prev = None 
        unique = set()
        while temp:
            if temp.data in unique:
                prev.pointer = temp.pointer
            else:
                unique.add(temp.data)
                prev = temp 
            temp = temp.pointer
        return temp
        
    

my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()
my_linked_list.print_nodes()
    
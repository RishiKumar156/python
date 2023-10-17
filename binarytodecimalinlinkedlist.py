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
        if not self.head:
            self.head = create_node
        else:
            temp = self.head 
            while temp.pointer:
                temp = temp.pointer
            temp.pointer = create_node
        self.length += 1
        return temp
    
    def print_nodes(self):
        temp = self.head 
        if not self.head:
            return None 
        else:
            while temp:
                print(temp.data)
                temp = temp.pointer 
    
    def  binary_to_decimal(self):
        prev = None 
        temp = self.head 
        result = 0 
        while temp:
            next_node = temp.pointer
            temp.pointer = prev 
            prev = temp
            temp = next_node
        self.head = prev 
        sums = self.head 
        # while sums:
        #     print(sums.data)
        #     sums = sums.pointer
        for i in range(self.length):
            result += (sums.data*2**i)
            sums = sums.pointer
        return result

linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(1)
# linked_list.append(0)
result = linked_list.binary_to_decimal()
print(f'Sums of the binary {result}')
        
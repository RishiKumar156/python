class Node():
    def __init__(self,data) -> None:
        self.data = data 
        self.pointer = None 
        
    
class LinkedList():
    def __init__(self,data) -> None:
        cnode = Node(data)
        self.head = cnode
        self.tail = cnode
        # we have to find the kth element from the end of linked list 
        
    def append(self, data):
        cnode = Node(data)
        if not self.head :
            self.head = cnode
            self.tail = cnode
        else:
            self.tail.pointer = cnode
            self.tail = cnode
            
    
def return_the_reversed_kth_element(self,k):
    faster = self.head 
    slower = self.head 
    for _ in range(k):
        if not faster:
            return None
        faster = faster.pointer
    while faster:
        slower = slower.pointer 
        faster = faster.pointer 
    return slower 
mynode = LinkedList(1)
mynode.append(2)
mynode.append(3)
mynode.append(4)
k = 1
result = return_the_reversed_kth_element(mynode, k)
print(result.data)
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.right = None 
        self.left = None 
    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
    
    def __r_insert(self,current_node, value):
        if not current_node:
            return Node(value) 
        if value > current_node.value:
            current_node.right =  self.__r_insert(current_node.right, value)
        if value < current_node.value:
            current_node.left =  self.__r_insert(current_node.left, value)
        return current_node
    
    def _insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root,value)
    
mynode = BinarySearchTree()
mynode._insert(3)
mynode._insert(5)
mynode._insert(4)
mynode._insert(2)
print(mynode.root.left.value)
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None 
        self.right = None 
    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None 

    def __r_insert(self,cnode,value):
        if not cnode:
            return Node(value)
        if cnode.value == value:
            return False 
        if value > cnode.value:
            cnode.right = self.__r_insert(cnode.right,value)
        if value < cnode.value:
            cnode.left = self.__r_insert(cnode.left,value)
        return cnode
        
    def _insert(self,value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root,value)
    
    def _r_contains(self,temp,value):
        if not temp:
            return False
        if temp.value == value:
            return True
        if value > temp.value:
            return self._r_contains(temp.right, value)
        if value < temp.value:
            return self._r_contains(temp.left, value)
        
    def contains(self,value):
        return self._r_contains(self.root,value)

mynode = BinarySearchTree()
mynode._insert(5)
mynode._insert(4)
mynode._insert(3)
mynode._insert(6)
mynode._insert(6)
mynode._insert(786)
print(mynode.root.left.left.value)
print(mynode.contains(7826))
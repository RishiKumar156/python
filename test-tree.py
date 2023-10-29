class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None 
        self.right = None 
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None 
    
    def _insert(self, temp ,value):
        if not temp:
            return Node(value)
        if value > temp.value:
            temp.right = self._insert(temp.right, value)
        if value < temp.value:
            temp.left = self._insert(temp.left, value)
        return temp
    
    def _r_insert(self,value):
        if not self.root:
            self.root = Node(value)
        return self._insert(self.root,value)
    
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
        return self._r_contains(self.root , value)

mynode = BinarySearchTree()
mynode._r_insert(5)
mynode._r_insert(3)
mynode._r_insert(786)
print(mynode.root.right.value)
print(mynode.contains(7861))
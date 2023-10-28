class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None 
        self.right = None 
    
class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None 
    
    def _insert(self,value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            temp = self.root
            while temp:
                if temp.value > new_node.value:
                    if not temp.left:
                        temp.left = new_node
                        return
                    temp = temp.left
                if temp.value < new_node.value:
                    if not temp.right:
                        temp.right = new_node
                        return
                    temp = temp.right
                    
    def __r_contains(self,temp, value):
        if not temp:
            return False 
        if temp.value == value:
            return True
        if value > temp.value:
            return self.__r_contains(temp.right, value)
        if value > temp.value:
            return self.__r_contains(temp.left, value)
    
    def r_contains(self,value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, value):
        new_node = Node(value)
        temp = self.root
        if not temp:
            self.root = new_node
            return
        if new_node.value > temp.value:
            return self.__r_insert(temp.right, value)
        else:
            if not temp.left:
                temp.left = new_node
                return
            temp = temp.left
            
    def r_insert(self,value):
        return self.__r_insert(value)
    
mynode = BinarySearchTree()
mynode._insert(3)
mynode._insert(5)
mynode._insert(2)
mynode._insert(786)
mynode._insert(186)
print(mynode.root.right.right.value)
print(mynode.r_contains(3))
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
        temp = self.root 
        if not self.root:
            self.root = new_node
            return 
        while temp:
            if new_node.value == temp.value:
                return None 
            if new_node.value > temp.value:
                if not temp.right: 
                    temp.right = new_node 
                    return
                temp = temp.right 
            if new_node.value < temp.value:
                if not temp.left :
                    temp.left = new_node
                temp = temp.left 
                
    def __r_contains(self, temp ,value):
        if temp.value == None or not temp.value:
            return False  
        if temp.value == value:
            return True
        if value > temp.value:
            """If value does not matched then move to next value 
            if condition we check wether the value is greater than
            the temp value if so then we pass the temp.right (Means right node of the
            temp value that's what appening)
                   (3)
                  /   \
                (1)    (4)
                        \
                        (5)
"""
            return self.__r_contains(temp.right,value) 
        if value < temp.value:
            """Here we check the value is lesser than the value then we just pass the temp.left node
            to the recursive opereation."""
            return self.__r_contains(temp.left , value)
    
    def r_contain(self,value):
        return self.__r_contains(self.root, value)
mytree = BinarySearchTree()
mytree._insert(3)
mytree._insert(4)
mytree._insert(5)
mytree._insert(1)
mytree._insert(16)
print(mytree.root.right.right.right.value)
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
    
    def __r_contains(self, value):
        temp = self.root
        if value < temp.value:
            temp = temp.left 
        if value > temp.value:
            temp = temp.right
    
    def _r_contains(self,value):

mytree = BinarySearchTree()
mytree._insert(3)
mytree._insert(4)
mytree._insert(5)
mytree._insert(1)
mytree._insert(16)
print(mytree.root.right.right.right.value)
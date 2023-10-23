class Node:
    def __init__(self,data) -> None:
        self.value = data
        self.left = None 
        self.right = None 


class BinaryTree:
    def __init__(self) -> None:
        self.root = None 
    
    def insert(self,value):
        create_node = Node(value)
        if not self.root:
            self.root = create_node
            return True 
        temp = self.root
        while True:
            if create_node.value == temp.value:
                return None 
            if create_node.value < temp.value:
                if not temp.left:
                    temp.left = create_node
                    return True
                temp = temp.left 
            else:
                if not temp.right:
                    temp.right = create_node
                    return True 
                temp = temp.right 
                
mytree = BinaryTree()

print(mytree.root)
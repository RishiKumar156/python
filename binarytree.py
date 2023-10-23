class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

class Binarytree:
    def __init__(self) -> None:
        self.root = None 

    def insert(self,value):
        create_node = Node(value)
        if not self.root:
            self.root = create_node 
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
            
mytree = Binarytree()
mytree.insert(1)
mytree.insert(2)
mytree.insert(3)

print(mytree.root.value)
print(mytree.root.right.value)
print(mytree.root.right.right.value)

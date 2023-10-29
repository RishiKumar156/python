class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None 
        self.right = None 

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None 
    
    def r_insert(self,temp,value):
        if not temp:
            return Node(value)
        if temp.value == value:
            return False 
        if value > temp.value:
            temp.right = self.r_insert(temp.right, value)
        if value < temp.value:
            temp.left = self.r_insert(temp.left, value)
        return temp
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.r_insert(self.root, value)
    
    def r_contains(self,temp,value):
        if not temp:
            return False 
        if temp.value == value:
            return True 
        if value > temp.value:
            return self.r_contains(temp.right,value)
        if value < temp.value:
            return self.r_contains(temp.left,value)
    
    def contains(self,value):
        return self.r_contains(self.root, value)
    
    ## WRITE DELETE_NODE METHODS HERE ##
    def __delete_node(self,temp,value):
        if not temp:
            return None 
        if value < temp.value:
            temp.left = self.__delete_node(temp.left, value)
        elif value > temp.value:
            temp.right = self.__delete_node(temp.right,value)
        else:
            if not temp.left and not temp.right:
                return None 
            elif not temp.left:
                temp = temp.right 
            elif not temp.right:
                temp = temp.left 
            else:
                find_min = self.min_value(temp.right)
                temp.value = find_min 
                temp.right = self.__delete_node(temp.right, find_min)
            return temp
    
    def delete_node(self,value):
        return self.__delete_node(self.root,value)
    
    def BFS(self):
        current_node = self.root 
        queue = []
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result

    def dfs_pre_order(self):
        result = []
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
    def dfs_inorder(self):
        result = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return result
    
mynode = BinarySearchTree()
mynode.insert(5)
mynode.insert(45)
mynode.insert(3)
print(mynode.contains(3))
print(f'BFS{mynode.BFS()}')
print(mynode.root.right.value)
print(mynode.dfs_pre_order())
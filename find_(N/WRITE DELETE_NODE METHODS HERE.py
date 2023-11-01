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
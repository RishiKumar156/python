class Solution:
        
    def deleteNode(self,head, x):
        # Code here
        def get(node,x):
            tt = node
            for _ in range(x-1):
                tt = tt.next
            return tt
        temp = get(head,x)
        if x == 1:
            new_node = head
            new_node = new_node.next
            new_node.prev = None
            return new_node
        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev 
        temp.next = None 
        temp.prev = None 
        return temp
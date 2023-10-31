def fractionalNodes(head,k):
        #add code here
        l = 0 
        temp = head 
        while temp:
            l += 1
            temp = temp.next 
        crnt = head
        find = l-k
        for _ in range(find):
            crnt = crnt.next 
        return crnt.data

print(fractionalNodes())
class MinHeap:
    def __init__(self) -> None:
        self.heap = []
        
    def _lef(self,index):
        return 2 * index + 1
    
    def _right(self, index):
        return 2 * index + 2 
    
    def _swap(self, idx1 , idx2):
        self.heap[idx1] , self.heap[idx2] = self.heap[idx2] , self.heap[idx1]
    
    def _parent(self , find_parent):
        return (find_parent - 1) // 2
    
    def _insert(self,value):
        self.heap.append(value)
        current_index = len(self.heap) - 1 
        while current_index > 0 and self.heap[current_index] < self.heap[self._parent(current_index)]:
            self._swap(current_index , self._parent(current_index))
            current_index = self._parent(current_index)
            

mynode = MinHeap()
mynode._insert(3)
mynode._insert(4)
mynode._insert(4)
mynode._insert(5)
print(mynode.heap)
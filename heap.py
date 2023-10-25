class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def _left_child(self,index):
        return 2 * index + 1
    
    def _right_child(self,index):
        return 2 * index + 2 
    
    def _parent(self,index):
        return (index - 1) // 2
    
    def _swap(self,index1 , index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1 
        while current_index > 0 and self.heap[current_index] > self.heap[self._parent(current_index)]:
            self._swap(current_index , self._parent(current_index))
            current_index = self._parent(current_index)
    
    def _sink_down(self,index):
        incoming_index = index
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        while True:
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[incoming_index]):
                incoming_index = left_index
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[incoming_index]):
                incoming_index = right_index
            if incoming_index != index :
                self._swap(index , incoming_index)
                index = incoming_index
            else:
                return
        
    def _remove(self):
        if len(self.heap) == 0:
            return None 
        if len(self.heap) == 1:
            return self.heap.pop()
        first_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return first_value
myheap = MaxHeap()
myheap._insert(14)
myheap._insert(1)
myheap._insert(114)
myheap._remove()
print(myheap.heap)
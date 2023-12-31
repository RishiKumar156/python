class MaxHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def _left_child(self,index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2 
    
    def _parent(self,index):
        return (index -1)//2 
    
    def _swap(self, index1,index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def _insert(self, value):
        self.heap.append(value)
        current_value = len(self.heap) - 1 
        while current_value > 0 and self.heap[current_value] > self.heap[self._parent(current_value)]:
            self._swap(current_value , self._parent(current_value))
            current_value = self._parent(current_value)
    
    def _sink_down(self,index):
        incoming_index = index
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        while True:
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[incoming_index]):
                incoming_index = left_index
                
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[incoming_index]):
                incoming_index = right_index
            
            if incoming_index != index:
                self._swap(index , incoming_index)
                index = incoming_index
            else:
                return 
            
    def remove(self):
        if not self.heap:
            return None 
        if len(self.heap) == 1:
            return self.heap.pop()
        
        first_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return first_item

mynode = MaxHeap()
mynode._insert(14)
mynode._insert(4)
mynode._insert(114)
mynode.remove()
print(mynode.heap)
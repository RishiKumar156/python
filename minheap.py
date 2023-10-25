class MinHeap:
    def __init__(self) -> None:
        self.heap = []
    
    def _left_child(self,index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2 
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def _insert(self, value):
        self.heap.append(value)
        current_item_index = len(self.heap) - 1 
        while current_item_index > 0 and self.heap[current_item_index] < self.heap[self._parent(current_item_index)]:
            self._swap(current_item_index , self._parent(current_item_index))
            current_item_index = self._parent(current_item_index)
    
    def _sink_up(self,index):
        incoming_index = index
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        while True:
            if(left_index < len(self.heap) and self.heap[left_index] < self.heap[self._parent(left_index)]):
                incoming_index = left_index
                
            if(right_index < len(self.heap) and self.heap[right_index] < self.heap[self._parent(right_index)]):
                incoming_index = right_index
                
            if incoming_index != index:
                self._swap(index , incoming_index)
                index = incoming_index
            else:
                return 
    def remove(self):
        if len(self.heap) == 0:
            return None 
        if len(self.heap) == 1:
            return self.heap.pop()
        first_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_up(0)
        return first_value
    
myheap = MinHeap()
myheap._insert(12)
myheap._insert(10)
myheap._insert(8)
myheap._insert(6)
myheap._insert(4)
myheap._insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]



"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]

"""
            
            
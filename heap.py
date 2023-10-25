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
            
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._lef(index)
            right_index = self._right(index)
            if left_index < len(self.heap) and self.heap[left_index] < self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] < self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return 

def make_to_max_heap(nums , k ):
    heap = MinHeap()
    for i in range(k):
        heap.heap.append(nums[i])
    for i in range(k , len(nums)):
        heap.heap[0] = nums[i]
    return heap.heap
mynode = MinHeap()
mynode._insert(3)
mynode._insert(4)
mynode._insert(4)
mynode._insert(5)
# print(mynode.heap)
print(make_to_max_heap([5,4,3,2] , 3))
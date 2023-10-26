class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _left_child(self,index):
        return 2 * index + 1 
    
    def _right_child(self,index):
        return 2 * index + 2 
    
    def _parent(self, index):
        return (index -1)//2 
    
    def _swap(self, index1, index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1]
    
    def _insert(self,value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        while current_index > 0 and self.heap[current_index] > self.heap[self._parent(current_index)]:
            self._swap(current_index , self._parent(current_index))
            current_index = self._parent(current_index)
    
    def _sink_down(self,index):
        incoming_index = index 
        while True:
            left_index = self._left_child(incoming_index)
            right_index = self._right_child(incoming_index)
            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[self._parent(left_index)]):
                incoming_index = left_index
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[self._parent(right_index)]):
                incoming_index = right_index
            if incoming_index != index:
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
        return first_value
    
###### WRITE STREAM_MAX FUNCTION HERE ######
def stream_max(nums):
    max_heap = MaxHeap()
    result = []
    for i in nums:
        max_heap._insert(i)
        result.append(max_heap.heap[0])
    return result
    
test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')


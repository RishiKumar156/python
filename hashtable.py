class HastTable:
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size
    
    def _hash(self, key):
        my_hash = 0 
        for letters in key:
            my_hash = (my_hash + ord(letters) * 23) % len(self.data_map)
        return my_hash
    
    def set_item(self, key , value):
        index = self._hash(key)
        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key,value])
        
    def get_item(self,key):
        index = self._hash(key)
        if not self.data_map[index]:
            return None
        else:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
                
    def print_maps(self):
        for i , j in enumerate(self.data_map):
            print(i , ':' , j)
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
mymap = HastTable()
mymap.set_item('tan' , 1000)
mymap.set_item('ate' , 2000)
mymap.set_item('tea' , 2000)
mymap.set_item('eat' , 1000)
mymap.set_item('nat' , 25000)
print(mymap.keys())
print(mymap.get_item('limber'))
mymap.print_maps()
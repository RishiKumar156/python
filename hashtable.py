class HastTable:
    def __init__(self, size = 7) -> None:
        self.data_map = [None] * size
    
    def _hash(self, key):
        my_hash = 0 
        for letters in key:
            my_hash = (my_hash + ord(letters) * 23) % len(self.data_map)
        return my_hash
    
    def print_maps(self):
        for i , j in enumerate(self.data_map):
            print(i , ':' , j)
    
mymap = HastTable()
mymap.print_maps()
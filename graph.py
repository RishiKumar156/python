class Graph:
    def __init__(self) -> None:
        self.adj_vertex = {} 
    
    def print_vertex(self):
        for i, v in self.adj_vertex.items():
            print(i, ':' ,v)
            
    def add_Vertex(self,vertex):
        if vertex not in self.adj_vertex.keys():
            self.adj_vertex[vertex] = []
            return True 
        return False 

    def add_edge(self, v1 , v2):
        if v1 and v2 in self.adj_vertex.keys():
            self.adj_vertex[v1].append(v2)
            self.adj_vertex[v2].append(v1)
            return True 
        return False 
    
    def remove_edge(self,v1,v2):
        if v1 and v2 in self.adj_vertex.keys():
            try:
                self.adj_vertex[v1].remove(v2)
                self.adj_vertex[v2].remove(v1)
            except ValueError:
                pass
            return True 
        return False 

    def remove_vertex(self,vertex):
        if vertex in self.adj_vertex.keys():
            for other_vertex in self.adj_vertex[vertex]:
                self.adj_vertex[other_vertex].remove(vertex)
            del self.adj_vertex[vertex]
            return True 
        return False 
    
mygraph = Graph()
mygraph.add_Vertex('A')
mygraph.add_Vertex('B')
mygraph.add_Vertex('C')
mygraph.add_edge('A','B')
mygraph.add_edge('A','C')
# mygraph.remove_edge('C' , 'A')
mygraph.remove_vertex('C')
mygraph.print_vertex()


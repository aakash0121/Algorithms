from collections import defaultdict

class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = set()
        self.num_vertices = 0
    
    def print_num_vertices(self):
        return self.num_vertices
    
    def print_vertices(self):
        return self.vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
        self.num_vertices = len(self.vertices)
                
    
    def DFSUtil(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    
    def find_mother_vertex(self):
        visited = [False for i in range(self.num_vertices)]
        v = 0

        for i in range(self.num_vertices):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                v = i

        visited = [False]*self.num_vertices
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return
        else:
            print("mother vertex is: " + str(v))
            return

if __name__ == "__main__":
    g = Graph() 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 3) 
    g.addEdge(4, 1) 
    g.addEdge(6, 4) 
    g.addEdge(5, 6) 
    g.addEdge(5, 2) 
    g.addEdge(6, 0) 
    print(g.print_num_vertices())
    g.find_mother_vertex()
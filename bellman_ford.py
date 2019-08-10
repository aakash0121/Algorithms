class Graph(object):
    def __init__(self):
        self.graph = []
        self.vertices = set()
        

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self.vertices.add(u)
        self.vertices.add(v)
        self.num_vertices = len(self.vertices)

    def print_num_vertices(self):
        print(self.num_vertices)
    
    def print_vertices(self):
        print(self.vertices)

    def print_distances(self, dist):
        for i in range(self.num_vertices):
            print(i, dist[i])
    
    def Bellman_Ford(self, src):
        dist = [float("inf")]*self.num_vertices
        dist[src] = 0

        for i in range(self.num_vertices):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[v] > dist[u] + w:
                print("A negative cycle is detected")
                return
        
        self.print_distances(dist)

if __name__ == "__main__":
    g = Graph() 
    g.addEdge(0, 1, -1) 
    g.addEdge(0, 2, 4) 
    g.addEdge(1, 2, 3) 
    g.addEdge(1, 3, 2) 
    g.addEdge(1, 4, 2) 
    g.addEdge(3, 2, 5) 
    g.addEdge(3, 1, 1) 
    g.addEdge(4, 3, -3)
    # g.print_num_vertices()
    # g.print_vertices()
    g.Bellman_Ford(0)

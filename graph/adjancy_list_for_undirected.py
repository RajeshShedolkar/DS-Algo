# Problem: Given the adjacency list and number of vertices and edges of a graph, 
# the task is to represent the adjacency list for a undirected graph.
# Ex. Input: V = 3, edges[][]= {{0, 1}, {1, 2} {2, 0}}

class Graph:
    def __init__(self):
        self.graph = dict()
    
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        
        if v not in self.graph:
            self.graph[v] = [u]
        else:
            self.graph[v].append(u)
    
    def printList(self):
        for index, vertex in enumerate(self.graph):
            print(f"vertex: {vertex}, Edges: {self.graph[vertex]}")

g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(4, 3)

g.printList()




class Graph:
    def __init__(self):
        self.graph = dict()
    
    def addEdge(self, u, v):
        
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
    
    def printList(self):
        for _, v in enumerate(self.graph):
            print(v, self.graph[v])


g = Graph()
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(4, 3)

g.printList()
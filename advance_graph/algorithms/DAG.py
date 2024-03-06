from collections import defaultdict


class DirectedEdge:
    def __init__(self,v,w,weight) -> None:
        self.v = v
        self.w = w
        self.weight = weight
    
    @property
    def Weight(self):
        return self.weight
    
    @property
    def From(self):
        return self.v
    
    @property
    def To(self):
        return self.w
    
    def __str__(self) -> str:
        return f"{self.v}->{self.w} {self.weight}"
    

class EdgeWeightedDiGraph:
    def __init__(self, number) -> None:
        self.V = number
        self.E = 0
        self.adj = defaultdict(list)
        for i in range(number):
            self.adj[i] = []
    
    def addEdge(self, edge:DirectedEdge):
        self.adj[edge.From].append(edge)
        self.E += 1

    def adj(self, v):
        return self.adj[v]
    
    def edges(self):
        temp = []
        for i in self.adj:
            for j in self.adj[i]:
                temp.append(i)
        return temp
    
    def __str__(self) -> str:
        temp = ""
        visited = set()
        for v in self.adj:
            for edge in self.adj[v]:
                if not (edge.From) in visited:
                    temp += str(edge) + "\n"
            visited.add((v))
        return temp
        
    
graph = EdgeWeightedDiGraph(5)
graph.addEdge(DirectedEdge(0,1,1.1))
graph.addEdge(DirectedEdge(1,2,2.2))
graph.addEdge(DirectedEdge(2,3,3.3))
graph.addEdge(DirectedEdge(3,4,4.4))
graph.addEdge(DirectedEdge(0,5,5.5))

print(graph)
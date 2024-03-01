from collections import defaultdict


class Edge:
    def __init__(self,v,w,weight) -> None:
        self.v = v
        self.w = w
        self.weight = weight

    @property
    def Weight(self):
        return self.weight
    
    def either(self):
        return self.v

    def other(self,vertex):
        if not vertex in [self.v, self.w]:
            raise ValueError(f"{vertex} does not exists")
        return self.w if self.v == vertex else self.w
    
    def compareTo(self, that):
        if self.weight > that.weight:
            return 1
        elif self.weight < that.weight:
            return -1
        return 0
    
    def toString(self):
        return f"{self.w}-{self.v} {self.weight}"
    
class EdgeWeightedGraph:
    def __init__(self, v) -> None:
        self.vertices = v
        self.edges = 0
        self.adj_list = defaultdict(list)
        for i in range(v):
            self.adj_list[i] = []

    @property
    def root(self):
        return self.root
    
    def addEdge(self, edge:Edge):
        v = edge.either()
        w = edge.other(v)
        self.adj_list[v].append(edge)
        self.adj_list[w].append(edge)
        self.edges += 1

    def __str__(self) -> str:
        temp = ""
        visited = set()
        for v in self.adj_list:
            for edge in self.adj_list[v]:
                if not (edge.v, edge.w) in visited:
                    temp += edge.toString() + "\n"
                    visited.add((edge.v,edge.w))
        return temp

    

graph = EdgeWeightedGraph(5)
graph.addEdge(Edge(0,1,1.1))
graph.addEdge(Edge(1,2,2.2))
graph.addEdge(Edge(2,3,3.3))
graph.addEdge(Edge(3,4,4.4))
graph.addEdge(Edge(0,5,5.5))

print(graph)

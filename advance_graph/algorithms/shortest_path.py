from collections import defaultdict
from heapq import heappop, heappush
import pytest


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
    
class DijkstraSP:
    def __init__(self, g: EdgeWeightedDiGraph, v: int) -> None:
        visited = set()
        pq = []
        cost = defaultdict(lambda:float("inf"))
        edges_map = defaultdict()
        cost[v] = 0
        heappush(pq, (0, v))
        while pq:
            _, vertex = heappop(pq)
            visited.add(vertex)
            for edge in g.adj[vertex]:
                if edge.To in visited:
                    continue
                newcost = cost[vertex] + edge.weight
                if cost[edge.To] > newcost:
                    cost[edge.To] = newcost
                    edges_map[edge.To] = vertex
                    heappush(pq, (newcost, edge.To))
        self.cost = cost
        self.paths = edges_map

    def distTo(self, v):
        return self.cost[v]
    
    def hasPathTo(self, v):
        return not self.cost[v] == float('inf')
        
    def pathTo(self, v):
        temp = [v]
        while v in self.paths:
            v= self.paths[v]
            temp.append(v)
        return temp
    
class DijkstraAllPairsSP:
    def __init__(self, g: EdgeWeightedDiGraph) -> None:
        self.allPairs = defaultdict()
        for v in range(g.V):
            self.allPairs[v] = DijkstraSP(g,v)
    
    def path(self,s,t):
        return self.allPairs[s].pathTo(t)
    
    def dist(self, s,t):
        return self.allPairs[s].distTo(t)
      
graph = EdgeWeightedDiGraph(8)
graph.addEdge(DirectedEdge(0,4,0.38))
graph.addEdge(DirectedEdge(0,2,0.26))
graph.addEdge(DirectedEdge(6,0,0.58))
graph.addEdge(DirectedEdge(7,5,0.28))
graph.addEdge(DirectedEdge(7,3,0.39))
graph.addEdge(DirectedEdge(5,7,0.28))
graph.addEdge(DirectedEdge(4,7,0.37))
graph.addEdge(DirectedEdge(2,7,0.34))
graph.addEdge(DirectedEdge(1,3,0.29))
graph.addEdge(DirectedEdge(5,1,0.32))
graph.addEdge(DirectedEdge(6,2,0.40))
graph.addEdge(DirectedEdge(3,6,0.52))
graph.addEdge(DirectedEdge(5,4,0.35))
graph.addEdge(DirectedEdge(4,5,0.35))
graph.addEdge(DirectedEdge(6,4,0.93))

print(graph)

sp = DijkstraSP(graph, 0)
assert sp.distTo(6) == pytest.approx(1.51, 1e-6)
assert sp.hasPathTo(6) == True
assert sp.pathTo(6) == [6, 3, 7, 2, 0]

allP = DijkstraAllPairsSP(graph)
assert allP.path(0,6) == [6, 3, 7, 2, 0]
assert allP.dist(0,6) == pytest.approx(1.51, 1e-6)

assert allP.path(0,3) == [3, 7, 2, 0]
assert allP.dist(0,3) ==pytest.approx(.99, 1e-6)

assert allP.path(3,7) == [7, 2, 6, 3]
assert allP.dist(3,7) == 1.26

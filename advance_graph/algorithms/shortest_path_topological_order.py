from collections import defaultdict, deque
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
        self._edges = []
        self.adj = defaultdict(list)
        for i in range(number):
            self.adj[i] = []
    
    def addEdge(self, edge:DirectedEdge):
        self.adj[edge.From].append(edge)
        self.E += 1
        self._edges.append(edge)

    def adj(self, v):
        return self.adj[v]
    
    def edges(self):
        return self._edges
    
    def __str__(self) -> str:
        temp = ""
        visited = set()
        for v in self.adj:
            for edge in self.adj[v]:
                if not (edge.From) in visited:
                    temp += str(edge) + "\n"
            visited.add((v))
        return temp
    
class TopologicalOrder:
    def __init__(self, g:EdgeWeightedDiGraph) -> None:
        self.reversepost = deque()
        visited = [False] * (g.V + 1)
        for i in range(graph.V):
            if visited[i] == False:
                self._dfs(i, visited, g)

    def _dfs(self,v:int, visited:list, graph:EdgeWeightedDiGraph):
        visited[v] = True
        edge = None
        for i in graph.adj[v]:
            edge = i
            if visited[i.To] == False:
                self._dfs(i.To, visited, graph)
        if edge:
            self.reversepost.append(edge) 

    @property
    def PreOrder(self):
        return self.pre
    
    @property
    def PostOrder(self):
        return self.post
    
    @property
    def ReversePostOrder(self):
        return self.reversepost
    

class AcyclicSP:
    def __init__(self, graph: EdgeWeightedDiGraph, v) -> None:
        visited = set()
        pq = []
        cost = defaultdict(lambda:float("inf"))
        for i in range(graph.V):
            cost[i] = float("inf")
        edges_map = defaultdict()
        cost[v] = 0
        pq = TopologicalOrder(graph).ReversePostOrder
        while pq:
            edge = pq.pop()
            visited.add(edge.From)
            for sedge in graph.adj[edge.From]:
                if edge.To in visited:
                    continue
                newcost = cost[sedge.From] + sedge.weight
                if cost[sedge.To] > newcost:
                    cost[sedge.To] = newcost
                    edges_map[sedge.To] = sedge
                    pq.append(sedge)
        self.distTo = cost
        self.edgeTo = edges_map


        """
        edgeTo = defaultdict()
        distTo = defaultdict()
        for v in range(graph.V):
            distTo[v] = float('inf')
        distTo[s] = 0.0
        tp = TopologicalOrder(graph)
        x = len(tp.ReversePostOrder) -1
        while x > 0:
            edge = tp.ReversePostOrder[x]
            for subedge in graph.adj[edge.From]:
                v = edge.From
                w = edge.To
                if distTo[w] > distTo[v] + edge.weight:
                    distTo[w] = distTo[v] + edge.weight
                    edgeTo[w] = edge
            x -= 1
        self.edgeTo = edgeTo
        self.distTo = distTo
        """
      
graph = EdgeWeightedDiGraph(8)
graph.addEdge(DirectedEdge(4,0,0.38))
graph.addEdge(DirectedEdge(0,2,0.26))
graph.addEdge(DirectedEdge(6,0,0.58))
graph.addEdge(DirectedEdge(3,7,0.39))
graph.addEdge(DirectedEdge(5,7,0.28))
graph.addEdge(DirectedEdge(4,7,0.37))
graph.addEdge(DirectedEdge(7,2,0.34))
graph.addEdge(DirectedEdge(1,3,0.29))
graph.addEdge(DirectedEdge(5,1,0.32))
graph.addEdge(DirectedEdge(6,2,0.40))
graph.addEdge(DirectedEdge(3,6,0.52))
graph.addEdge(DirectedEdge(5,4,0.35))
graph.addEdge(DirectedEdge(6,4,0.93))

print(graph)

acyclic = AcyclicSP(graph,5)
assert acyclic.distTo[6] == pytest.approx(1.13)





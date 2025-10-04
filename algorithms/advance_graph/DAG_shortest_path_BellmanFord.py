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

class BellmanFordSP:
    def __init__(self, graph: EdgeWeightedDiGraph, s) -> None:
        self.edgeTo = defaultdict()
        self.distTo = defaultdict()
        onQueue = defaultdict()
        queue = deque()
        for v in range(graph.V):
            self.distTo[v] = float('inf')
        self.distTo[s] = 0.0
        queue.append(s)
        onQueue[s] = True
        while queue and not self.hasNegativeCycle():
            v = queue.pop()
            onQueue[v] = False
            for edge in graph.adj[v]:
                w = edge.To
                if self.distTo[w] > self.distTo[v] + edge.weight:
                    self.distTo[w] = self.distTo[v] + edge.weight
                    self.edgeTo[w] = edge
                    if w not in onQueue.keys() or not onQueue[w]:
                        queue.append(w)
                        onQueue[w] = True
            if all([value != float("inf") for value in self.distTo.values()]):
                self.findNegativeCycle(graph)
    
    def hasNegativeCycle(self) -> bool:
        try:
            return self.cf.cycle
        except AttributeError:
            return False
    
    def findNegativeCycle(self, graph:EdgeWeightedDiGraph):
        spt = EdgeWeightedDiGraph(graph.V)
        for i in range(graph.V):
            if i in self.edgeTo:
                spt.addEdge(self.edgeTo[i])
        self.cf = DirectedCycle(spt)
        return self.cf
    
class DirectedCycle:
    def __init__(self, g:EdgeWeightedDiGraph) -> None:
        self.grap = graph
        self.cycle = []
        self.edgeTo = {}
        visited = [False] * g.V
        stack = []
        for v in self.grap.adj:
            if visited[v] == False:
                self._dfs(v,visited, stack)

    def _dfs(self,v:int, visited:list, stack:list):
        visited[v] = True
        stack.append(v)
        for i in self.grap.adj[v]:
            if self.HasCycle():
                return
            elif visited[i.To] == False:
                self.edgeTo[i.To] = v
                self._dfs(i.To,visited, stack)
            elif i.To in stack:
                cycle = []
                x = v
                while x != i.To:
                    cycle.append(x)
                    x= self.edgeTo[x]
                cycle.append(i)
                self.cycle.append(cycle)
        stack.pop()

    def HasCycle(self):
        return len(self.cycle) != 0
      
graph = EdgeWeightedDiGraph(8)
graph.addEdge(DirectedEdge(4,5,0.35))
graph.addEdge(DirectedEdge(5,4,0.35))
graph.addEdge(DirectedEdge(4,7,0.37))
graph.addEdge(DirectedEdge(5,7,0.28))
graph.addEdge(DirectedEdge(7,5,0.28))
graph.addEdge(DirectedEdge(5,1,0.32))
graph.addEdge(DirectedEdge(0,4,0.38))
graph.addEdge(DirectedEdge(0,2,0.26))
graph.addEdge(DirectedEdge(7,3,0.39))
graph.addEdge(DirectedEdge(1,3,0.29))
graph.addEdge(DirectedEdge(2,7,0.34))
graph.addEdge(DirectedEdge(6,2,-1.20))
graph.addEdge(DirectedEdge(3,6,0.52))
graph.addEdge(DirectedEdge(6,0,-1.40))
graph.addEdge(DirectedEdge(6,4,-1.25))

#print(graph)

acyclic = BellmanFordSP(graph,0)
assert acyclic.distTo[6] == pytest.approx(1.13)
print(acyclic.distTo)





from collections import defaultdict, deque
from heapq import *
from math import inf


class Edge:
    def __init__(self,v,w,weight) -> None:
        self.v = v
        self.w = w
        self.weight = weight
    def __gt__(self, other):
        if self.weight > other.weight:
            return True
        return False

    @property
    def Weight(self):
        return self.weight
    
    def either(self):
        return self.v

    def other(self,vertex):
        if not vertex in [self.v, self.w]:
            raise ValueError(f"{vertex} does not exists")
        return self.w if self.v == vertex else self.v
    
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
        self.edges = []
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
        self.edges.append(edge)

    def __str__(self) -> str:
        temp = ""
        visited = set()
        for v in self.adj_list:
            for edge in self.adj_list[v]:
                if not (edge.v, edge.w) in visited:
                    temp += edge.toString() + "\n"
                    visited.add((edge.v,edge.w))
        return temp

class LazyPrimMST:
    def __init__(self, graph: EdgeWeightedGraph) -> None:
        weightmap = {}
        for edge in graph.edges:
            weightmap[edge.weight] = edge
        self.edges = []
        min_heap = []
        visited = []
        for edge in graph.adj_list[0]:
            heappush(min_heap, edge)
        visited.append(0)
        while min_heap:
            min = heappop(min_heap)
            if min.v in visited and min.w in visited:
                continue
            self.edges.append(min)
            if min.v in visited:
                visited.append(min.w)
                for edge in graph.adj_list[min.w]:
                    heappush(min_heap, edge)
            else:
                visited.append(min.v)
                for edge in graph.adj_list[min.v]:
                    heappush(min_heap, edge)    
        self.vertices = len(visited)
    
    @property
    def Edges(self):
        return self.edges
    
    @property
    def Vertices(self):
        return self.vertices

class EagerPrimMST:
    def __init__(self, graph: EdgeWeightedGraph) -> None:
        self.pq_map = defaultdict()
        self.pq = []
        self.edgeTo = defaultdict()
        self.distTo = defaultdict()
        self.visited = []
        for i in range(len(graph.adj_list)):
            self.distTo[i] = inf
        self.distTo[0] = 0.0
        self.visited.append(0)
        heappush(self.pq, (0.0,0))
        while self.pq:
            weight, vertex = heappop(self.pq)
            self.BFS(graph, vertex)        

    def BFS(self, graph, vertex):
        if not vertex in self.visited:
            self.visited.append(vertex)
        for edge in graph.adj_list[vertex]:
            w = edge.other(vertex)
            if w in self.visited:
                continue
            if edge.weight < self.distTo[w]:
                self.edgeTo[w] = edge
                self.distTo[w] = edge.weight
                if w in self.pq:
                    self.pq_map[w] = self.distTo[w]
                else:
                    heappush(self.pq, (self.distTo[w], w))
                    self.pq_map[w] = self.distTo[w]

    @property
    def Edges(self):
        return self.edgeTo.values()
    
    @property
    def Vertices(self):
        return self.visited
    
graph = EdgeWeightedGraph(5)
graph.addEdge(Edge(0,4,0.38))
graph.addEdge(Edge(0,7,0.16))
graph.addEdge(Edge(0,2,0.26))
graph.addEdge(Edge(0,6,0.58))
graph.addEdge(Edge(7,1,0.19))
graph.addEdge(Edge(7,5,0.28))
graph.addEdge(Edge(7,4,0.37))
graph.addEdge(Edge(7,2,0.34))
graph.addEdge(Edge(1,2,0.36))
graph.addEdge(Edge(1,3,0.29))
graph.addEdge(Edge(1,5,0.32))
graph.addEdge(Edge(2,3,0.17))
graph.addEdge(Edge(2,6,0.40))
graph.addEdge(Edge(3,6,0.52))
graph.addEdge(Edge(5,4,0.35))
graph.addEdge(Edge(4,6,0.93))

print(graph)

mst = EagerPrimMST(graph)

assert set([edge.toString() for edge in mst.Edges]) == set(['7-0 0.16', '1-7 0.19', '2-0 0.26', '3-2 0.17', '5-7 0.28', '4-5 0.35', '6-2 0.4'])
mst.Vertices == [0, 7, 1, 2, 3, 5, 4, 6]

from collections import defaultdict
from collections import deque
from typing import List


class UnDirectedGraph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self, u,v):
        self.graph[u].append(v)


class Paths:
    def __init__(self, G: UnDirectedGraph, s:int, approach: str= "dfs") -> None:
        self.graph = G
        self.source = s
        self.visited = {}
        self.edgeTo = {}
        for key in G.graph.keys():
            self.visited[key] = False
        if approach == "bfs":
            self.bfs(s)
        else:
            self.dfs(s)

    def hasPathTo(self, v: int) -> bool:
        return self.visited[v] == True
    
    def dfs(self,vertex):
        if vertex not in self.visited:
            self.visited[vertex] = False
        if not self.visited[vertex]:
            self.visited[vertex] = True
            for neighbor in self.graph.graph[vertex]:
                self.edgeTo[neighbor] = vertex
                self.dfs(neighbor)
    
    def bfs(self,vertex):
        tempq = []
        self.visited[vertex]= True
        tempq.append(vertex)
        while tempq:
            v = tempq.pop()
            for neighbor in self.graph.graph[v]:
                if not neighbor in self.visited:
                    self.visited[neighbor] = False
                if not self.visited[neighbor]:
                    self.edgeTo[neighbor] = v
                    self.visited[neighbor] = True
                    tempq.append(neighbor)

    def pathTo(self, v: int) -> List[int]:
        if not self.visited[v]:
            return None
        path = deque()
        path.appendleft(v)
        while v != self.source:
            v = self.edgeTo[v]
            path.appendleft(v)
        return list(path)

        


if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = UnDirectedGraph()
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 5)
    g.addEdge(3, 4)


    p = Paths(g, 0, "bfs")
    assert p.hasPathTo(2) == True
    assert p.pathTo(3) == [0,2,3]


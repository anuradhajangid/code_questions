from collections import defaultdict
from collections import deque
from typing import List


class UnDirectedGraph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self, u,v):
        if v is not None:
            self.graph[u].append(v)
        else:
            self.graph[u] = []


class Cycle:
    def __init__(self, G: UnDirectedGraph) -> None:
        self.graph = G
        self.hasCycle = False
        self.visited = {}
        for key in G.graph.keys():
            self.visited[key] = False
        for v in self.graph.graph:
            if not v in self.visited:
                self.visited[v] = False
            if not self.visited[v]:
                self.dfs(-1,v)
    
    def dfs(self, u, v):
        
        if not self.visited[v]:
            self.visited[v] = True
            for neighbor in self.graph.graph[v]:
                if neighbor not in self.visited:
                    self.visited[neighbor] = False
                if not self.visited[neighbor]:
                    self.dfs(v, neighbor)
                elif (neighbor != u):
                    self.hasCycle = True
    

    def hasCycle(self):
        return self.hasCycle == True



if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = UnDirectedGraph()
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(1, 0)


    p = Cycle(g)
    assert p.hasCycle == True


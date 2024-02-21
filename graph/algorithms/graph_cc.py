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


class CC:
    def __init__(self, graph:UnDirectedGraph) -> None:
        visited = [False] * (max(graph.graph)+1)
        self.graph = g.graph
        self.id = {}
        self.count = 0
        for i in graph.graph:
            if visited[i] == False:
                self._dfs(i, visited, self.count)
                self.count += 1

    def _dfs(self, vertex, visited, count):
        visited[vertex] = True
        self.id[vertex] = count
        for i in self.graph[vertex]:
            if visited[i] == False:
                self._dfs(i, visited, count)

    def Connected(self, v, w):
        return self.id[v] == self.id[w]

    def ID(self, v):
        return self.id[v]
    
    def Count(self):
        return self.count



if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = UnDirectedGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 6)
    g.addEdge(0, 5)
    g.addEdge(2, 0)
    g.addEdge(1, 0)
    g.addEdge(3, 5)
    g.addEdge(3, 4)
    g.addEdge(4, 3)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 0)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(6, 0)
    g.addEdge(6, 4)
    g.addEdge(7, 8)
    g.addEdge(8, 7)
    g.addEdge(9, 10)
    g.addEdge(9, 11)
    g.addEdge(9, 12)
    g.addEdge(10, 9)
    g.addEdge(11, 9)
    g.addEdge(11, 12)
    g.addEdge(12, 9)
    g.addEdge(12, 11)


    c = CC(g)
    assert c.Count() == 3
    assert c.Connected(6,9) == False
    assert c.Connected(1,4)


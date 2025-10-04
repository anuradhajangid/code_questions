from collections import defaultdict
from collections import deque


class Digraph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.e = []
    
    @property
    def V(self):
        return list(self.graph.keys())
    
    @property
    def E(self):
        return self.e

    def addEdge(self, fr:int, to:int) -> None:
        if to:
            self.graph[fr].append(to)
            self.E.append((fr,to))
        else:
            self.graph[fr] = []

    def BFS(self,s:int) -> None:
        stack = []
        visited = [False] * (max(self.graph) + 1)
        stack.append(s)
        print(s, end="")
        visited[s] = True
        while stack:
            temp = stack.pop(0)
            for x in self.graph[temp]:
                if visited[x] == False:
                    print(x, end="")
                    visited[x] = True
                    stack.append(x)
        return 
                

    def DFS(self,s:int) -> None:
        visited = [False] * (max(self.graph) + 1)
        def helper(vertex:int, visited:list):
            visited[vertex] = True
            print(vertex, end="")
            for i in self.graph[vertex]:
                if visited[i] == False:
                    helper(i, visited)
        helper(s,visited)
        return
    
    
    def Reverse(self):
        reverse = Digraph()
        for i in self.graph:
            for w in self.graph[i]:
                if w not in reverse.graph:
                    reverse.graph[w] = []
                reverse.e.append((w,i))
                reverse.graph[w].append(i)
        return reverse
    
class DepthFirstOrder:
    def __init__(self, g:Digraph) -> None:
        self.grap = g.graph
        self.pre = deque()
        self.post = deque()
        self.reversepost = deque()
        visited = [False] * (max(g.graph) + 1)
        for i in self.grap:
            if visited[i] == False:
                self._dfs(i, visited)

    def _dfs(self,v:int, visited:list):
        self.pre.append(v)
        visited[v] = True
        for i in self.grap[v]:
            if visited[i] == False:
                self._dfs(i, visited)
        self.post.append(v)
        self.reversepost.append(v)

    @property
    def PreOrder(self):
        return self.pre
    
    @property
    def PostOrder(self):
        return self.post
    
    @property
    def ReversePostOrder(self):
        return self.reversepost
    
        
if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = Digraph()
    g.addEdge(0, 5)
    g.addEdge(0, 1)
    g.addEdge(0, 6)
    g.addEdge(1,None)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 5)
    g.addEdge(4, None)
    g.addEdge(5, 4)
    g.addEdge(6, 4)
    g.addEdge(6, 9)
    g.addEdge(7, 6)
    g.addEdge(8, 7)
    g.addEdge(9, 11)
    g.addEdge(9, 12)
    g.addEdge(9, 10)
    g.addEdge(10, None)
    g.addEdge(11, 12)
    g.addEdge(12, None)

 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    dc = DepthFirstOrder(g)
    assert list(dc.pre) == [0,5,4,1,6,9,11,12,10,2,3,7,8], dc.PreOrder
    assert list(dc.post) == [4,5,1,12,11,10,9,6,0,3,2,7,8], dc.PostOrder
    assert dc.reversepost == deque([4, 5, 1, 12, 11, 10, 9, 6, 0, 3, 2, 7, 8]), dc.ReversePostOrder
from collections import defaultdict


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
        self.graph[fr].append(to)
        self.E.append((fr,to))

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
    
class DirectedCycle:
    def __init__(self, g:Digraph) -> None:
        self.grap = g.graph
        self.cycle = []
        self.edgeTo = {}
        visited = [False] * (max(g.graph) + 1)
        stack = []
        for v in g.graph:
            if visited[v] == False:
                self._dfs(v,visited, stack)

    def _dfs(self,v:int, visited:list, stack:list):
        visited[v] = True
        stack.append(v)
        for i in self.grap[v]:
            if self.HasCycle():
                return
            elif visited[i] == False:
                self.edgeTo[i] = v
                self._dfs(i,visited, stack)
            elif i in stack:
                cycle = []
                x = v
                while x != i:
                    cycle.append(x)
                    x= self.edgeTo[x]
                cycle.append(i)
                self.cycle.append(cycle)
        stack.pop()

    def HasCycle(self):
        return len(self.cycle)
    
    def Cycle(self):
        return self.cycle




        
        
        
if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = Digraph()
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    dc = DirectedCycle(g)
    print(dc.HasCycle())
    print(dc.Cycle())
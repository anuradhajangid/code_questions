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
if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = Digraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.DFS(2)
    print(g.V)
    print(g.E)
    reverse = g.Reverse()
    reverse.DFS(2)
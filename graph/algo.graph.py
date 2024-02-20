from collections import defaultdict


class UnDirectedGraph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self, u,v):
        #Adds connectivity to both vertices
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s= queue.pop(0)
            print(s, end="")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    def DFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        def helper(vertex, visited):
            visited[vertex] = True
            print(vertex, end="")
            for i in self.graph[vertex]:
                if visited[i] == False:  
                    helper(i, visited)
        helper(s, visited)
        


if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = UnDirectedGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
 
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)


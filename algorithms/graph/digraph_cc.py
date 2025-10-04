from collections import defaultdict
from collections import deque


from collections import defaultdict

#Ref: https://lucyliu-ucsb.github.io/posts/Kosaraju-Compute-SCC/

class Graph:
    
    def __init__(self, adj_lst):        
        self.graph = adj_lst  
    
    def addEdge(self, vertex1, vertex2): # add an edge from vertex1 to vertex2
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        if vertex2 is not None:
            self.graph[vertex1].append(vertex2)

    
    def reverseGraph(self):        
        inverseG = Graph(defaultdict(list))
        
        for i in self.graph:
            for j in self.graph[i]:
                inverseG.addEdge(j, i)
        return inverseG

    def finishingTimeStack(self, vertex, visited, stack):
        '''
        visited: a dict to record visited vertices
        vertex: current vertex 
        stack: push vertex to stack as DFS proceeding
        '''
        visited[vertex] = True
        for i in self.graph[vertex]:
            if visited[i] == False:
                self.finishingTimeStack(i, visited, stack)
        stack.append(vertex)
    
    def getOneSCC(self, vertex, visited, scc):
        scc.append(vertex)
        visited[vertex] = True
        
        for v in self.graph[vertex]:
            if visited[v] == False:
                self.getOneSCC(v, visited, scc)
    
    def computeSCCs(self):
        
        stack = [] # order of stack is the finishing time
        
        ### First DFS: compute the finishing time
        visited = defaultdict(bool) # initialized all notes as unvisited
        
        for i in list(self.graph.keys()): # use outer loop to ganrantee every note will be visited
            if visited[i] == False:
                self.finishingTimeStack(i, visited, stack)
        
        ### Compute a inverse graph
        inverG = self.reverseGraph()
        
        ### Second DFS: compute the SCCs
        SCC_lst = []
        visited =  defaultdict(bool) # initialized all notes as unvisited 
        while stack:
            i = stack.pop()
            if visited[i] == False:
                scc = []
                inverG.getOneSCC(i, visited, scc)
                SCC_lst.append(scc)
        return SCC_lst

    
        
if __name__ == '__main__':
 
    # Create a graph given in
    # the above diagram
    g = Graph(
defaultdict(list,
            {7: [1],
             4: [7],
             1: [4],
             9: [7, 3],
             6: [9],
             8: [6, 5],
             2: [8],
             5: [2],
             3: [6]}))

    print(g.computeSCCs())
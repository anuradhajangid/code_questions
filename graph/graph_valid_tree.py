#https://leetcode.com/problems/graph-valid-tree/
from collections import defaultdict


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def DFS(u,v):
            if visited[v] == False:
                visited[v] = True
                for neighbour in graph[v]:
                    if visited[neighbour] == False:
                        DFS(v, neighbour)
                    elif neighbour != u:
                        cycle[0] = True

        graph = defaultdict(list)
        cycle = [False]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        count = n-len(graph)
        if count > 1:
            return False
        visited = [False] * n
        for vertex in graph:
            if visited[vertex] == False:
                DFS(-1,vertex)
                count += 1
        return count == 1 and not cycle[0]
        
        
assert Solution().validTree(5, [[0,1],[0,2],[0,3],[1,4]]) == True
assert Solution().validTree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]]) == False
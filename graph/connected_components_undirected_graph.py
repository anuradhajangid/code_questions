#https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
from collections import defaultdict


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def DFS(vertex):
            visited[vertex] = True
            for neighbour in graph[vertex]:
                if visited[neighbour] == False:
                    DFS(neighbour)

        #Create graph
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        count = n-len(graph)
        visited = [False] * n
        for vertex in graph:
            if visited[vertex] == False:
                DFS(vertex)
                count += 1
        return count



        
assert Solution().countComponents(5,[[0,1],[1,2],[3,4]]) == 2
assert Solution().countComponents(5,[[0,1],[1,2],[2,3],[3,4]]) == 1

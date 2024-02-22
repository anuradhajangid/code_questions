#https://leetcode.com/problems/redundant-connection/description/

from collections import defaultdict, deque


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        def DFS(u,v):
            if u in visited:
                return False
            if u == v:
                return True
            visited.add(u)
            for neighbor in graph[u]:
                if DFS(neighbor, v):
                    return True    
            return False
        
        graph = defaultdict(list)
        cycle = []
        
        for x,y in edges:
            visited = set()
            if DFS(x,y):
                cycle.append([x,y])
            graph[x].append(y)
            graph[y].append(x)
    
        
        return cycle[-1]


assert Solution().findRedundantConnection([[1,2],[1,3],[2,3]]) == [2,3]
assert Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1,4]
assert Solution().findRedundantConnection([[1,4],[3,4],[1,3],[1,2],[4,5]]) == [1,3]

#https://leetcode.com/problems/network-delay-time/description/
from collections import defaultdict
from heapq import heappop, heappush


class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        #Shortest path 
        #Create a graph
        graph = defaultdict(list)
        for s, t, w in times:
            graph[s].append((t,w))
        pq = []
        dist = [-float("inf")] * n
        dist[k-1] = 0
        heappush(pq, (0,k))
        while pq:
            weight, vertex = heappop(pq)
            for edge, edgeweight in graph[vertex]:
                if weight + edgeweight > dist[edge-1] :
                    dist[edge-1] = weight + edgeweight  
                    heappush(pq, (dist[edge-1], edge))
        longest_path = max(dist)
        shortest_path = min(dist)
        if shortest_path != -float("inf"):
            return longest_path
        return -1
                


        
assert Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2) == 2
assert Solution().networkDelayTime([[1,2,1]], n = 2, k = 1) == 1
assert Solution().networkDelayTime([[1,2,1]], n = 2, k = 2) == -1
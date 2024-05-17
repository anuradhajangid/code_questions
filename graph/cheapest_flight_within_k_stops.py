#https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
from collections import defaultdict, deque
from typing import List

class WeightedDiGraph:
    def __init__(self, edges_weight) -> None:
        self.adj_list = defaultdict(list)
        self.edgeTo = defaultdict()
        self.V = 0

        for fr, to, weight in edges_weight:
            self.adj_list[fr].append((to, weight))

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.graph = WeightedDiGraph(flights) #TODO
        mincost = float("inf")

        #BFS to find the dest from source in K stops
        searchQueue = deque()
        searchQueue.append((src, 0, 0))
        while searchQueue:
            node, stops, cost = searchQueue.popleft()
            if stops-1 > k:
                continue
            if node == dst:
                mincost = min(mincost, cost)
            for neighbour in self.graph.adj_list[node]:
                searchQueue.append((neighbour[0], stops + 1, cost + neighbour[1]))
        if mincost == 0:
            return -1
        return mincost


assert Solution().findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1) == 700
assert Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1) == 200
assert Solution().findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0) == 500

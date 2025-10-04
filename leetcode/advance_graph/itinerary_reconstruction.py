#https://leetcode.com/problems/reconstruct-itinerary/description/
from collections import defaultdict
import heapq


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        starting = "JFK"
        graph  = defaultdict(list)
        path = []
        for fr,to in tickets:
            temp = graph[fr]
            heapq.heappush(temp,to)
        def dfs(port):
            while graph[port]:
                dfs(heapq.heappop(graph[port]))
            path.append(port)
        dfs(starting)
        return path[::-1]
        

assert Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]) == ["JFK","MUC","LHR","SFO","SJC"]
assert Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]) == ["JFK","ATL","JFK","SFO","ATL","SFO"]

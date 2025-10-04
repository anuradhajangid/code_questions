from typing import List
from collections import defaultdict, deque
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        bob_times = []
        def bob_dfs(src, prev, time):
            if src == 0:
                bob_times[src] = time
                return True
            for nei in adj[src]:
                if src == prev:
                    continue
                if bob_dfs(nei, src, time+1):
                    bob_times[src] = time
        bob_dfs(bob, -1, 0)

        res = float("-inf")
        queue = deque()
        queue.append(0, -1, 0, amount[0])
        while queue:
            src, prev, time, profit = queue.pop()
            for nei in adj[src]:
                if nei == prev:
                    continue                    
                nei_profit = amount[nei]
                if nei in bob_times:
                    if bob_times[nei] < time + 1:
                        nei_profit = 0
                    if bob_times[nei] == time + 1:
                        nei_profit = amount[nei]//2
                queue.append(nei, src, time+1, profit+nei_profit)
                if len(adj[nei]) == 1:
                    res = max(profit + nei_profit, res)
        return res
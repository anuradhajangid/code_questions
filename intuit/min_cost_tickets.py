from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i == len(days):
                return 0
            memo[i] = float("inf")
            for d, cost in zip([1,7,30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j+=1
                memo[i] = min(dfs(j), cost + dfs(j))
            
        dfs(0)
        return memo[0]
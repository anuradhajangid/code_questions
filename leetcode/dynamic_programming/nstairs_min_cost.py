#https://leetcode.com/problems/min-cost-climbing-stairs/description/
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.dynamicTopDown(cost,len(cost),2, float("inf"))

    def dynamicTopDown(self,cost,n,m,mincost):
        """
        TimeComplexity = m * n
        Space Complexity = n
        """
        memo = {}
        min = float("inf")
        def _recursive(n, m, memo):
            # base case
            if n == 0:
                return cost[n]
            # check in memo
            if n in memo:
                return memo[n]
            ways = 0
            for i in range(1, m+1):
                if i <= n:
                    ways += _recursive(n-i,m,memo)
            memo[n] = ways
            min = min(min, ways)
            return ways, min
        return _recursive(n, m, memo)

assert Solution().minCostClimbingStairs(cost = [10,15,20]) == 15
assert Solution().minCostClimbingStairs(cost = [1,100,1,1,1,100,1,1,100,1]) == 6
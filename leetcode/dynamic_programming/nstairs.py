import datetime
#https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # m = 2
        return self.dynamicTopDown(n,2)

    def dynamicTopDown(self,n,m):
        """
        TimeComplexity = m * n
        Space Complexity = n
        """
        memo = {}
        def _recursive(n, m, memo):
            # base case
            if n == 0:
                return 1
            # check in memo
            if n in memo:
                return memo[n]
            ways = 0
            for i in range(1, m+1):
                if i <= n:
                    ways += _recursive(n-i,m,memo)
            memo[n] = ways
            return ways
        return _recursive(n, m, memo)

    
    def bruteForce(n,m):
        """
        Time complexity  = m**n
        Space complexity = constant
        """
        results = [0]
        def recursive(cLocation, cPath):
            cPath.append(cLocation)
            if cLocation == n:
                results[0] += 1
                return
            for i in range(1,m+1):
                if cLocation + i <=n:
                    recursive(cLocation+i,cPath)
            return 
        recursive(0,[])
        return results[0]

assert Solution().climbStairs(2) == 2
assert Solution().climbStairs(3) == 3
assert Solution().climbStairs(12) == 233
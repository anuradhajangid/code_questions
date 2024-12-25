from typing import List
class Solution:
    def catalan_recursion(self,n):
        """
        Time Complexity = O(n!)
        Space complexity = O(1)
        """

        if n == 0:      # base case; C(0) = 1
            return 1
        sum = 0
        # iterate from 1...n to evaluate: C(0)*C(n-1) + C(1)*C(n-2) ... + C(n-1)*C(0)
        for i in range(n):  
            sum += (self.catalan_recursion(i) * self.catalan_recursion(n-1-i))  # C(i)*C(n-1-i)
        return sum

    def catalan_memoization(self, n):
        """
        Time Complexity = O(n*2)
        Space complexity = O(n)
        """
        memo = {}
        def helper(n):
            if n == 0:
                return 1
            if n in memo:
                return memo[n]
            sum = 0
            for i in range(n):
                sum += (self.catalan_memoization(i) * self.catalan_memoization(n-i-1))
            memo[n] = sum
            return sum
        return helper(n)   
    def catalan_tabulation(self, n):
        """
        Time Complexity = O(n*2)
        Space complexity = O(n)
        """
        table = [None] * (n+1)
        table[0] = 1
        for i in range(1, n+1):
            table[i] = 0
            for j in range(i):
                table[i] += table[j] * table[i-j-1]
        return table[n]

    
assert Solution().catalan_recursion(4) == 14
assert Solution().catalan_memoization(4) == 14
assert Solution().catalan_tabulation(4) == 14
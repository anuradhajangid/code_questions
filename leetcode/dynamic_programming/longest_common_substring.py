from typing import List
class Solution:
    def lcs_recursion(self,str1, str2):
        """
        TimeComplexity = O(3**(m+n))
        SpaceComplexity = O(1)
        """
        def helper(str1, str2, i, j, count):
            if i >= len(str1) or j >= len(str2):
                return count
            if str1[i] == str2[j]:
                count = helper(str1, str2, i+1, j+1, count+1)
            return max(count, helper(str1, str2, i , j+1, 0), helper(str1, str2, i+1, j, 0))
        return helper(str1, str2, 0, 0, 0)
    
    def lcs_memoization(self,str1, str2):
        """
        TimeComplexity = O(m*n*2)
        SpaceComplexity = O(m*n)
        """
        memo = {}
        def helper(str1, str2, i, j, count):
            if i >= len(str1) or j>=len(str2):
                return count
            if (i, j, count) in memo:
                return memo[(i,j,count)]
            c = count
            if str1[i] == str2[j]:
                c= helper(str1, str2, i+1, j+1, count+1)
            memo[(i, j, count)] = max(c, helper(str1, str2, i+1, j, 0), helper(str1, str2, i, j+1, 0))
            return memo[i, j, count]
        return helper(str1, str2, 0, 0, 0)
    
    def lcs_tabulation(self, str1, str2):
        """
        TimeComplexity = O(m*n)
        SpaceComplexity = O(m*n)
        """
        n = len(str1)
        m = len(str2)
        table = [[0 for i in range(m+1)] for j in range(n+1)]
        maxlen = 0
        for i in range(1,n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    table[i][j] = table[i-1][j-1] + 1
                    maxlen = max(maxlen, table[i][j])
                else:
                    table[i][j] = 0
        return maxlen
    def lcs_tabulation_space_optimization(self, str1, str2):
        """
        TimeComplexity = O(m*n)
        SpaceComplexity = O(n) where n is max of the two strings
        """
        n = len(str1)
        m = len(str2)
        table = [0 for i in range(n+1)]
        maxlen = 0
        for j in range(1,m+1):
            current_row = [0 for k in range(n+1)]
            for i in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    current_row[i] = table[i-1] + 1
                    maxlen = max(maxlen, current_row[i])
                else:
                    current_row[i] = 0
            table = current_row
        return maxlen
                    
assert Solution().lcs_tabulation_space_optimization("abcde", "ace" ) == 1
assert Solution().lcs_tabulation_space_optimization("hello elf", "hello yourself") == 6
assert Solution().lcs_tabulation_space_optimization("hello", "elf") == 2
assert Solution().lcs_recursion("hello", "elf") == 2
assert Solution().lcs_recursion("hello elf", "hello yourself") == 6
assert Solution().lcs_memoization("hello", "elf") == 2
assert Solution().lcs_memoization("hello elf", "hello yourself") == 6
assert Solution().lcs_tabulation("hello", "elf") == 2
assert Solution().lcs_tabulation("hello elf", "hello yourself") == 6



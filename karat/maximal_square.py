#https://leetcode.com/problems/maximal-square/description/
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        cache = dict()

        def helper(row, col):
            nonlocal N
            nonlocal M
            nonlocal matrix

            if row >=N or col >= M:
                return 0
            
            if (row, col) not in cache:
                right = helper(row, col)
                down = helper(row+1, col)
                dia = helper(row+1, col+1)

                cache[(row,col)] = 0
                if matrix[row][col] == "1":
                    cache[row][col] = 1 + min(right, down, dia)

            return cache[(row,col)]
            
        helper(0,0)
        return max(cache.values()) ** 2



        

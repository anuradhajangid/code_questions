# https://leetcode.com/problems/toeplitz-matrix/description/?envType=problem-list-v2&envId=7p59281
from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

assert Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]) == True
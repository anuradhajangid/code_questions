#https://leetcode.com/problems/set-matrix-zeroes/
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        point = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    point.append((i,j))
        for i,j in point:
            for x in range(0, len(matrix[0])):
                matrix[i][x] = 0
            for x in range(0, len(matrix)):
                matrix[x][j] = 0
        return matrix
    
    def setZeros_M2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        point = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    point.append((i,j))
        for i,j in point:
            matrix[i] = [0]*len(matrix[0])
            for k in range(0,len(matrix)):
                matrix[k][j] = 0
        return matrix
    

assert Solution().setZeros_M2([[1,1,1,1,0],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,1,0],[1,0,0,1,0]]
    

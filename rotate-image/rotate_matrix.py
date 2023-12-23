#https://leetcode.com/problems/rotate-image/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) -1 
        mlen = len(matrix)
        for row in range(0, int(mlen/2)):
            for col in range(row, n-row):
                tmp = matrix[row][col]
                matrix[row][col] = matrix[n-col][row]
                matrix[n-col][row] = matrix[n-row][n-col]
                matrix[n-row][n-col] = matrix[col][n-row]
                matrix[col][n-row] = tmp
        

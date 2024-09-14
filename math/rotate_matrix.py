from typing import List

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
        return matrix

assert Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
assert Solution().rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
from typing import List
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        m=len(matrix[0])

        for i in range(n):
            row = set()
            for j in range(m):
                row.add(matrix[i][j])
            if len(row) != n:
                return False

        for j in range(m):
            col = set()
            for i in range(n):
                col.add(matrix[i][j])
            if len(col) != m:
                return False
        return True
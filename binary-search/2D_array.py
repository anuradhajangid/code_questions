from typing import List
#https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    def searchMatrixOp(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n -1 
        while start <= end:
            mid = (start + end)//2
            mid_row = int(mid/n)
            mid_col = mid%n
            if target == matrix[mid_row][mid_col]:
                return True
            elif target > matrix[mid_row][mid_col]:
                start = mid + 1
            else:
                end = mid - 1
        return False
    
s=Solution()
assert s.searchMatrixOp([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
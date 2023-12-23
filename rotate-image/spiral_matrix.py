#https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix) 
        cols = len(matrix[0])
        rs = 0
        re = rows-1
        
        cs = 0
        ce = cols-1
        splist = []

        while len(splist) < rows * cols:
            for i in range (cs, ce+1):
                splist.append(matrix[rs][i])
            rs += 1

            for i in range(rs, re+1):
                splist.append(matrix[i][ce])
            ce -= 1

            if rs <= re:
                for i in range(ce, cs-1, -1):
                    splist.append(matrix[re][i])
                re -= 1
            if cs <=ce:
                for i in range(re, rs-1, -1):
                    splist.append(matrix[i][cs])
                cs += 1
        return splist

            
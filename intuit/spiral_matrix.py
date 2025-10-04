from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        N = len(matrix)
        M = len(matrix[0])
        rs = 0
        re = N-1
        cs = 0
        ce = M-1

        splist = []

        while len(splist) < M*N:
            for i in range (cs, ce+1):
                splist.append(matrix[rs][i])
            rs += 1

            for i in range(rs, re+1):
                splist.append(matrix[i][ce])
            ce -= 1

            if re >= rs:
                for i in range(ce, cs-1, -1):
                    splist.append(matrix[re][i])
                re -= 1
            if ce >= cs:
                for i in range(re, rs-1, -1):
                    splist.append(matrix[i][cs])
                cs += 1
        return splist

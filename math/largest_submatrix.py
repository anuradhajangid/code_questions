class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        row = len(matrix)
        col = len(matrix[0])

        # Row sum
        for r in range(1, row):
            for c in range(col):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r-1][c]
        ans = 0
        # Col sum
        for r in range(row):
            matrix[r].sort(reverse=True)
            for c in range(col):
                ans = max(ans, (c+1) * matrix[r][c])

assert Solution().largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]) == 4
assert Solution().largestSubmatrix([[1,0,1,0,1]]) == 3

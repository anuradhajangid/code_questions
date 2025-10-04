import collections
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = collections.defaultdict(set())
        cols = collections.defaultdict(set())
        grids = collections.defaultdict(set())

        N = len(board)

        for row in range(N):
            for col in range(N):
                if board[row][col] ==".":
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in grids[(row//3, col//3)]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                grids[(row//3, col//3)].add(board[row][col])
        return True

        
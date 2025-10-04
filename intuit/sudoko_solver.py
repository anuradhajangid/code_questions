from typing import List
from collections import defaultdict
import numpy as np
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board = np.array(board)
        def helper (board, row, col):
            if col == 9:
                row +=1 
                col = 0
            if row == 9:
                return True
            if board[row][col] != ".":
                return helper(board, row, col+1)
            for num in range(1,10):
                if Solution().isvalid(board, str(num), row, col):
                    board[row, col] = str(num)
                    if helper(board, row, col+1):
                        return True
                    board[row,col] = "."
            return False
        helper(board, 0, 0)
        return 
    
        
    @staticmethod
    def isvalid(board, number, row, col):
        if number in board[row,:] or number in board[:,col] or number in board[row//3 * 3 : row//3 * 3 + 3, col//3 * 3: col//3 * 3 + 3]:
            return False
        return True


assert Solution().solveSudoku([
    [5,3,".",".",7,".",".",".","."],
    [6,".",".",1,9,5,".",".","."],
    [".",9,8,".",".",".",".",6,"."],
    [8,".",".",".",6,".",".",".",3],
    [4,".",".",8,".",3,".",".",1],
    [7,".",".",".",2,".",".",".",6],
    [".",6,".",".",".",".",2,8,"."],
    [".",".",".",4,1,9,".",".",5],
    [".",".",".",".",8,".",".",7,9]]) == True
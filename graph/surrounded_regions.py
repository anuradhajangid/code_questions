#https://leetcode.com/problems/surrounded-regions/description/
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        def dfs(row,col):
            if 0<=row<rows and 0<=col<cols and board[row][col] == "O":
                board[row][col] = "V"
                dfs(row,col+1)
                dfs(row,col-1)
                dfs(row+1,col) 
                dfs(row-1,col)
        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)
        for j in range(cols):
            dfs(0,j)
            dfs(rows-1,j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "V":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
        return board


board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
assert Solution().solve(board) == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
board = [["X"]]
assert Solution().solve(board) == [["X"]]
board = [["O","O"],["O","O"]]
assert Solution().solve(board) == [["O","O"],["O","O"]]
board = [["O","O","O"],["O","O","O"],["O","O","O"]]
assert Solution().solve(board) == [["O","O","O"],["O","O","O"],["O","O","O"]]
board = [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
assert Solution().solve(board) == [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","O"],["O","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","X"],["O","X","X","X","X","X","X","X","X","O"],["O","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
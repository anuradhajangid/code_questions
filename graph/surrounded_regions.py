#https://leetcode.com/problems/surrounded-regions/description/
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp = []
                if board[i][j] != "X":
                    Solution.dfs(i,j,board,temp)
                    if len(temp)> 1:
                        for (i,j) in temp:
                            board[i][j] = "X"
        return board
    @staticmethod
    def dfs(row, col, grid, path):
        if (row,col) in path:
            return
        if row < 0 or row > len(grid)-1 or col < 0 or col > len(grid[0])-1 or grid[row][col] in ["X"]: 
            return
        path.append((row,col))
        Solution.dfs(row,col+1,grid,path)
        Solution.dfs(row,col-1,grid,path)
        Solution.dfs(row+1,col,grid,path) 
        Solution.dfs(row-1,col,grid,path)

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
assert Solution().solve(board) == [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
board = [["X"]]
assert Solution().solve(board) == [["X"]]
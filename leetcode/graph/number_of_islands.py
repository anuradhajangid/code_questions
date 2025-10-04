#https://leetcode.com/problems/number-of-islands/
from collections import defaultdict

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "$" and grid[i][j] != "0":
                    count += 1
                    Solution.dfs(i,j,grid)
        return count
    
    def dfs(row, col, grid):
        if row < 0 or row > len(grid)-1 or col < 0 or col > len(grid[0])-1 or grid[row][col] in ["0", "$"]: 
            return
        grid[row][col] = "$"
        Solution.dfs(row,col+1,grid)
        Solution.dfs(row,col-1,grid)
        Solution.dfs(row+1,col,grid)
        Solution.dfs(row-1,col,grid)


s = Solution()
assert s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1
assert s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3

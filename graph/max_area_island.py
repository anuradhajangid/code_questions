#https://leetcode.com/problems/max-area-of-island/description/
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count = 0
                if grid[i][j] != "$" and grid[i][j] != 0:
                    count = Solution.dfs(i,j,grid,count)
                    maxarea = max(maxarea, count)
        return maxarea
    @staticmethod
    def dfs(row, col, grid, count):
        if row < 0 or row > len(grid)-1 or col < 0 or col > len(grid[0])-1 or grid[row][col] in [0, "$"]: 
            return 0
        grid[row][col] = "$"
        return 1 + Solution.dfs(row,col+1,grid,count) + Solution.dfs(row,col-1,grid,count) + Solution.dfs(row+1,col,grid,count) + Solution.dfs(row-1,col,grid,count)


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
assert Solution().maxAreaOfIsland(grid) == 6
grid = [[0,0,0,0,0,0,0,0]]
assert Solution().maxAreaOfIsland(grid) == 0

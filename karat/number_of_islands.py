#https://leetcode.com/problems/number-of-islands/description/
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        def dfs(i, j):
            nonlocal N
            nonlocal M
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            grid[i][j] = "*"

            for di, dj in directions:
                newi = i + di
                newj = j + dj
                if 0 <= newi < N and  0 <= newj < M and grid[newi][newj] == "1":
                    dfs(newi, newj)                   


        islands = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands
    

assert Solution().numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) == 1

assert Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) == 3
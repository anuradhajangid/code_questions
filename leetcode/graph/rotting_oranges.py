#https://leetcode.com/problems/rotting-oranges/description/

from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten,fresh = deque(),set()
        time = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        while fresh and rotten:
            for _ in range(len(rotten)):
                i, j = rotten.popleft()
                for cell in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if cell in fresh:
                        rotten.append(cell)
                        fresh.remove(cell)
                        
            time += 1
        return -1 if fresh else time

grid = [[2,1,1],[1,1,0],[0,1,1]]
assert Solution().orangesRotting(grid) == 4
grid = [[2,1,1],[0,1,1],[1,0,1]]
assert Solution().orangesRotting(grid) == -1
grid = [[0,2]]
assert Solution().orangesRotting(grid) == 0
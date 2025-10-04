from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        N = len(grid)
        M = len(grid[0])
        fresh = 0
        rotton = deque()
        time = 0
        visited = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    fresh += 1
                    continue
                if grid[i][j] == 2:
                    visited.add((i,j))
                    rotton.append((i,j, time))
        
        while fresh and len(rotton):
            row, col, time = rotton.popleft()
            for diri, dirj in directions:
                newrow = diri + row
                newcol = dirj + col
                if -1 < newrow < N and -1 < newcol < M and grid[newrow][newcol] == 1 and (newrow, newcol) not in visited:
                    visited.add((newrow,newcol))
                    fresh -= 1
                    rotton.append((newrow, newcol, time +1))
        if time:
            time += 1
        return -1  if fresh else time

assert Solution().orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]) == -1
assert Solution().orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]) == 4  
assert Solution().orangesRotting([[0,2]]) == 0 

            




#https://leetcode.com/problems/shortest-path-in-binary-matrix/description/?envType=problem-list-v2&envId=7p59281
from typing import List
from collections import deque
class Solution:
    # Time limit exceeds, for shortest distance between two points, use dijkistra or BFS
    def shortestPathBinaryMatrix_wrong(self, grid: List[List[int]]) -> int:
        min_path = float("inf")
        n = len(grid) -1
        path = []
        def dfs(i,j, path):
            nonlocal min_path
            path.append((i,j))
            if i == n and j == n and grid[i][j] == 0:
                if len(path) < min_path:
                    min_path = len(path)
                    return
                return
            for p,q in [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]:
                ni = i+p
                nj = j+q
                if 0 <= ni <= n and 0 <= nj <= n and (ni, nj) not in path and grid[ni][nj] == 0:
                    dfs(ni, nj, path)
                    path.pop()
        
        if grid[0][0] == 0:
            dfs(0,0,path)
        if min_path < float("inf"):
            return min_path
        return -1
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        n = len(grid) -1

        if grid[0][0] != 0:
            return -1
        visited = set()
        queue.append((0,0,1))
        visited.add((0,0))
        while queue:
            i,j,path = queue.popleft()
            if i == n and j == n and grid[i][j] == 0:
                return path
            for p, q in [(0,1), (0,-1), (1,0), (-1,0), (-1,-1), (-1,1), (1,-1), (1,1)]:
                ni = i+p
                nj = j+q
                if 0 <= ni <= n and 0 <= nj <= n and (ni, nj) not in visited and grid[ni][nj] == 0:
                  visited.add((ni,nj))
                  queue.append((ni,nj,path+1))
        return -1
assert Solution().shortestPathBinaryMatrix([[0,1,0,1,0],[1,0,0,0,1],[0,0,1,1,1],[0,0,0,0,0],[1,0,1,0,0]]) == 6
assert Solution().shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]) == -1
assert Solution().shortestPathBinaryMatrix([[0,1],[1,0]]) == 2
assert Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]) == 4
"""
Examples
[[0,0,0], [1,1,0], [1,1,0]]
min_path =  inf
visited = []
n=2
i=0
j=0
path = [(0,0), (0,1) (0,2)]

[[0,1],[1,0]]
min_path =  inf
n=1
i=0
j=0
path = [(0,0), (0,1) (0,2)]


"""
            
                

#https://leetcode.com/problems/swim-in-rising-water/description/
from collections import defaultdict
import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Shortest distance between source(0,0) and dest(l,l)
        row = len(grid)
        col = len(grid[0])
        # push source to min heap with weight as first element for min heap function
        pq = []
        visited = set((0,0))
        heapq.heappush(pq, (grid[0][0], 0,0))
        while pq:
            weight, i, j = heapq.heappop(pq)
            if i == row-1 and j == col -1:
                return weight
            for x,y in [[i-1,j], [i+1,j], [i,j-1], [i,j+1]]:
                if 0 <= x <row and 0 <= y < col:
                    if (x,y) not in visited:
                        heapq.heappush(pq, (max(weight, grid[x][y]), x, y)) 
                        visited.add((x,y))  





        
assert Solution().swimInWater([[0,2],[1,3]]) == 3
assert Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]) == 16


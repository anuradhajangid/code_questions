
#https://leetcode.com/problems/walls-and-gates/
from collections import deque


class Solution(object):
    INF = 2147483647
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        empty,gateFill = set(),deque()

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    gateFill.append((i, j))
                elif rooms[i][j] == Solution.INF:
                    empty.add((i, j))
        while empty and gateFill:
            for _ in range(len(gateFill)):
                i, j = gateFill.popleft()
                for cell in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if cell in empty:
                        rooms[cell[0]][cell[1]] = rooms[i][j] + 1
                        gateFill.append(cell)
                        empty.remove(cell)
        return rooms   
        


rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
assert Solution().wallsAndGates(rooms) == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
rooms = [[-1]]
assert Solution().wallsAndGates(rooms) == [[-1]]
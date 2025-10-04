import attrs
from typing import List

@attrs.define
class FireFighter:
    grid: List[List[int]]

    def distinguish_fire(self) ->None:
        islands = self.get_islands()
        islands.sort(key=len, reverse=True)
        return

    
    def get_islands(self):
        result = []
        visited = []
        row = len(self.grid)
        col = len(self.grid[0])

        def dfs(x, y, current):
            visited.append((x,y))
            if self.grid[x][y] == 0:
                return []
            current.append((x,y))
            for dx, dy in [(1,0), (-1,0), (0,1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if not (nx<0 or nx>= row or ny<0 or ny>= col) and (nx, ny) not in visited:
                    dfs(nx, ny, current)
            return current

        for i in range(row):
            for j in range(col):
                if not (i,j) in visited:
                    data = (dfs(i,j,[]))
                    if data:
                        result.append(data)
        return result


ff = FireFighter([[1,0,0], [0,0,1], [1,1,1]])
ff.distinguish_fire()
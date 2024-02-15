#https://www.educative.io/courses/grokking-coding-interview-patterns-python/flood-fill
def flood_fill(grid, sr, sc, target):
    orig = grid[sr][sc]
    visited = []
    fill(grid,sr,sc,target, orig, visited)
    return grid

def fill(grid, sr, sc, target, orig, visited):
    visited.append((sr,sc))
    if sr >= len(grid) or sr < 0 or sc >= len(grid[0]) or sc < 0:
        return
    if grid[sr][sc] == orig:
        grid[sr][sc] = target
    fill(grid, sr-1, sc, target, orig,visited) if ((0<= sr-1 < len(grid)) and (sr-1,sc) not in visited  and grid[sr-1][sc] == orig)else None
    fill(grid, sr+1, sc, target, orig,visited) if ((0<= sr+1 < len(grid)) and (sr+1,sc) not in visited and grid[sr+1][sc] == orig) else None
    fill(grid, sr, sc-1, target, orig,visited) if ((0<= sc-1 < len(grid[0])) and (sr,sc-1) not in visited  and grid[sr][sc-1] == orig) else None
    fill(grid, sr, sc+1, target, orig,visited) if ((0<= sc+1 < len(grid[0])) and (sr,sc+1) not in visited  and grid[sr][sc+1] == orig) else None
    return grid

# driver code
def main():
    inputs = [([[1,1,0,1,0],[0,0,0,0,1],[0,0,0,1,1],[1,1,1,1,0],[1,0,0,0,0]], 4, 3, 3), ([[3,3,6,3,6],[6,6,6,6,3],[6,6,6,3,3],[3,3,3,3,6],[3,6,6,6,6]], 4, 3, 7)]

    for (grid, row, col, target) in inputs:
        print(f"Input grid is: {grid}, row:{row}, col:{col}, target:{target}")
        print(flood_fill(grid, row, col, target))
        print("-" * 100)

if __name__ == '__main__':
    main()
#https://leetcode.com/problems/pacific-atlantic-water-flow/description/
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows,cols = len(heights),len(heights[0])

        #Helper for depth first search of the oceans water flow
        def dfs(i,j,visited,ocean):
            if i<0 or i>=rows or j<0 or j>=cols or visited[i][j] or heights[i][j] < ocean:
                return
            visited[i][j] = True
            dfs(i-1,j,visited,heights[i][j])
            dfs(i,j-1,visited,heights[i][j])
            dfs(i+1,j,visited,heights[i][j])
            dfs(i,j+1,visited,heights[i][j])
            return
        
        #Oceans with their respective water flow
        pf = [[False for _ in range(cols)] for _ in range(rows)]
        at = [[False for _ in range(cols)] for _ in range(rows)]
        
        #FloodFill pf and at oceans from from left and right respectively
        for i in range(rows):
            dfs(i,0,pf,0)
            dfs(i,cols-1,at,0)
        
        #Flood fill pf and at from top & bottom respectively
        for j in range(cols):
            dfs(0,j,pf,0)
            dfs(rows-1,j,at,0)
        
        #Find the intersection between two oceans
        res = []
        for i in range(rows):
            for j in range(cols):
                if pf[i][j] and at[i][j]:
                    res.append([i,j])
        return res
        
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
assert Solution().pacificAtlantic(heights) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
heights = [[1]]
assert Solution().pacificAtlantic(heights) == [[0,0]]
#https://leetcode.com/problems/min-cost-to-connect-all-points/description/
from collections import defaultdict, deque
from math import sqrt

class UnionFind:
    def __init__(self, n) -> None:
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, v):
        if self.parents[v] != v:
            self.parents[v] = self.find(self.parents[v])
        return self.parents[v]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.ranks[px] < self.ranks[py]:
                self.parents[px] = py
                self.ranks[py] += self.ranks[px]
            else:
                self.parents[py] = px
                self.ranks[px] += self.ranks[py]
            return True
        return False


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        #Krushkal algorith using union find
        l = len(points)
        edges =[]
        for i in range(l):
            for j in range(i+1, l):
                md = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((md, i, j))
        edges.sort()
        dsu = UnionFind(l)
        mstvalue = 0
        visited = 0
        for edge in edges:
            if visited == l - 1:
                break
            if dsu.union(edge[1], edge[2]):
                mstvalue += edge[0]
                visited += 1
        
        return mstvalue
            
        


        
assert Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
assert Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
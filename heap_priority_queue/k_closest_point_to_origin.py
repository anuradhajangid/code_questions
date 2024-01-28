# https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import *
from math import sqrt
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minpoints = []
        for (x,y) in points:
            distance = sqrt(x*x + y*y)
            heappush(minpoints, (distance, x,y))
        result = []
        for i in range(k):
            dist, x, y = heappop(minpoints)
            result.append((x,y))
        return(result)

print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))
        
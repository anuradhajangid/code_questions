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
        for i, (x,y) in enumerate(points):
            distance = sqrt(x*x + y*y)
            heappush(minpoints, (-distance, i))
            if len(minpoints) > k:
                heappop(minpoints)
        return [points[i] for _,i in minpoints]

assert (Solution().kClosest([[3,3],[5,-1],[-2,4]], 2)) == [[-2, 4], [3, 3]]
assert Solution().kClosest([[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]], 5) == [[17,7],[-2,-42],[53,20],[-36,-57],[-69,-8]]
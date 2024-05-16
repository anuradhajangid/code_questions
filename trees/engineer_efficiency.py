#https://leetcode.com/problems/maximum-performance-of-a-team/description/
from typing import List
from heapq import *
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        maxheap = []
        maxefficienfy = 0
        runningsum = 0
        for eff, sp in sorted(zip(efficiency, speed), reverse=True):
            runningsum += sp
            if len(maxheap)>=k:
                runningsum -= heappop(maxheap)
            heappush(maxheap, sp)
            maxefficienfy = max(maxefficienfy, runningsum * eff)
        return (maxefficienfy % (10**9+7))


assert Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2) == 60
assert Solution().maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3) == 68
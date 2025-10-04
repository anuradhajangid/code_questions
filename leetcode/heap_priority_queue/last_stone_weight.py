#https://leetcode.com/problems/last-stone-weight/

from heapq import *
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max = [-stone for stone in stones]
        heapify(max)
        while len(max)> 1:
            num1 = -heappop(max)
            num2 = -heappop(max)
            if num1 != num2:
                heappush(max, -(num1-num2))
        if max:
            return -max[0]
        return None

print(Solution().lastStoneWeight([2,7,4,1,8,1]))
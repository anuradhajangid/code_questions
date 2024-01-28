# https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        largest = []
        for num in nums:
            heappush(largest, -num)
        
        result = []
        for i in range(k):
            result.append(-heappop(largest))
        return result[-1]
    
print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))


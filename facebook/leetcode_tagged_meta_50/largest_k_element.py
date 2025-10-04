#https://leetcode.com/problems/kth-largest-element-in-an-array/?envType=problem-list-v2&envId=7p59281
from typing import List
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_stack = []
        for element in nums:
            if len(min_stack) > k:
                heappop(min_stack)
            heappush(min_stack, element)
        heappop(min_stack)
        return heappop(min_stack)

assert  Solution().findKthLargest([3,2,1,5,6,4], k = 2) == 5
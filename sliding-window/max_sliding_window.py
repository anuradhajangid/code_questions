#https://leetcode.com/problems/sliding-window-maximum/
from typing import List
from queue import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        custommax = []
        customqueue = deque()
        for i in range(len(nums)):
            if customqueue and customqueue[0] <= i - k:
                customqueue.popleft()
            while customqueue and nums[customqueue[-1]] <= nums[i]:
                customqueue.pop()
            customqueue.append(i)
            if i >= k-1:
                custommax.append(nums[customqueue[0]])
        return custommax

assert Solution().maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3) == [3,3,5,5,6,7]
#https://leetcode.com/problems/sliding-window-maximum/
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
        
#https://leetcode.com/problems/132-pattern/
from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mid = float ("-inf")
        nums = reversed(nums)
        stack = []
        for num in nums:
            if num < mid:
                return True
            while stack and stack[-1] < num:
                mid = stack.pop()
            stack.append(num)
        return False


assert Solution().find132pattern(nums = [1,2,3,4]) == False
assert Solution().find132pattern(nums = [3,1,4,2]) == True
assert Solution().find132pattern(nums = [-1,3,2,0]) == True
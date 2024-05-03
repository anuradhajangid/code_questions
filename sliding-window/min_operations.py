#https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

from math import inf
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        currentsum = 0
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        if nums[-1] == x or nums[0] ==x:
            return 1
        if x == 0:
            return -1
        if nums[0] + nums[-1] == x:
            return 2
        p1, p2, result= 0, 0, -1
        for p1, value in enumerate(nums):
            currentsum += value
            while currentsum > target:
                currentsum -= nums[p2]
                p2 += 1
            if currentsum == target:
                result = max(result, p1-p2+1)
        if result != -1:
            return (len(nums) - result)
        return -1
            
                

assert Solution().minOperations(nums = [1,1,4,2,3], x = 5) == 2
assert Solution().minOperations(nums = [5,6,7,8,9], x = 4) == -1
assert Solution().minOperations(nums = [3,2,20,1,1,3], x = 10) == 5
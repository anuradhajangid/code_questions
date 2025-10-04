#https://leetcode.com/problems/missing-ranges?envType=problem-list-v2&envId=7p59281
from typing import List

class Solution():
    def missingRanges(nums:List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[lower, upper]]
        if nums[0] > lower:
            res.append([lower,nums[0]])
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                res.append([nums[i]+1, nums[i+1]-1])
        if nums[-1] < upper:
            res.append([nums[-1]+1, upper])
        return res
    
    def missingRange_ii(nums:List[int], lower: int, upper: int):
        res = []
        current_lower = lower
        nums.append(upper)
        for i in range(len(nums) -1):
            diff = nums[i] - current_lower
            if  diff > 2:
                res.append(f"{current_lower}-{nums[i]-1}")
            elif diff == 2:
                res.append(f"{current_lower}")
                res.append(f"{nums[i] - 1}")
            elif diff == 1:
                res.append(f"{current_lower}")
            current_lower = nums[i] + 1
        return res

assert Solution().missingRanges()
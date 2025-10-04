from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            target = 0-nums[i]
            start = i+1
            end = len(nums) -1
            while start < end:
                if nums[start] + nums[end] == target and (nums[target], nums[start], nums[end]) not in result:
                    result.add((nums[target], nums[start], nums[end]))
                    start += 1
                if nums[start] + nums[end] > nums[target]:
                    end -=1
                else:
                    start += 1
        return len(result)

assert Solution().threeSum(nums = [-1,0,1,2,-1,-4]) == 3

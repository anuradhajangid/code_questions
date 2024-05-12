#https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/description/
from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        left = 0
        right = len(nums) -1
        while left < right:
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right -= 1
        if left == right:
            result.append(nums[right])
        return result
    
print(Solution().rearrangeArray([1,2,3,4,5]))
print(Solution().rearrangeArray([6,2,0,9,7]))
        
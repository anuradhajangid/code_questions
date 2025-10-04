#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums)-1
        if end == 0:
            return nums[0]
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = ( start + end )//2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            else:
                if nums[mid] > nums[end]:
                    start = mid
                else:
                    end = mid
        return nums[start]

s = Solution()
assert s.findMin([3,4,5,1,2]) == 1
assert s.findMin([1]) == 1
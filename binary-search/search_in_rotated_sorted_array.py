#https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = ( start + end )//2
            if nums[mid] == target:
                return mid
            else:
                if nums[start] <= nums[mid]:
                    if nums[start] <= target < nums[mid]:
                        end= mid-1
                    else:
                        start = mid + 1
                else:
                    if nums[mid] < target <= nums[end]:
                        start = mid + 1
                    else:
                        end = mid -1
                

        return -1
        
s = Solution()
assert s.search([4,5,6,7,0,1,2], 0) == 4
assert s.search([3,1], 3) == 0
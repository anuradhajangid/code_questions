#https://leetcode.com/problems/find-peak-element?envType=problem-list-v2&envId=7p5928
from typing import List
class Solution:
    def peakElement(self, arr:List[int]) -> int:
        left = 0
        right = len(arr) -1
        while left <= right:
            mid = left + (right -left )//2
            if mid >0 and arr[mid] < arr[mid -1]:
                right = mid - 1
            elif mid <len(arr) and arr[mid]< arr[mid+1]:
                left = mid + 1
            else:
                return mid

assert Solution().peakElement([1,2,3,4,3,2]) == 4
assert Solution().peakElement([1,2,3,1]) == 3
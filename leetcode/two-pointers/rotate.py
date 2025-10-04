from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def helper(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start +1, end -1
            return

        helper(0,len(nums)-1)
        helper(0,k-1)
        helper(k,len(nums)-1) 

        return nums

assert Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3) == [5,6,7,1,2,3,4]
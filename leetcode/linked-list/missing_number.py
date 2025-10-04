from typing import List
#https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicateRepeatingOnce(self, nums: List[int]) -> int:
        length = len(nums)
        maxsum = (length*(length+1))//2
        actualsum = sum(nums)
        return (length-(maxsum-actualsum))
    
    def findDuplicateRepeatingAny(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow


s= Solution()
print(s.findDuplicateRepeatingOnce([2,2,2,2]))
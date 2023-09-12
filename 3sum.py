#https://leetcode.com/problems/3sum/description/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        
        nums.sort()

        for i in range (0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            right = len(nums) -1
            left = i+1
            target_sum = 0-nums[i]
            while (left < right):
                
                if (nums[left] + nums[right]) == target_sum:
                    triplets.add((nums[i], nums[left], nums[right]))
                pl = left
                pr = right
                if target_sum - nums[left] < nums[right]:
                    right -= 1
                if target_sum - nums[right] > nums[left]:
                    left += 1
                if pl == left and pr == right:
                    left += 1
        return triplets
                
        
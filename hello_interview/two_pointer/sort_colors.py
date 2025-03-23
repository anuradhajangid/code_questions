class Solution:
    def sortColors(self, nums: list[int]):
        zero = 0
        one = 0
        two = len(nums) - 1
        while one <= two:
            if nums[one] == 2:
                nums[one], nums[two] = nums[two], nums[one]
                while two > one and nums[two] == 2:
                    two -= 1
            if nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
            one += 1
            
        return nums

assert Solution().sortColors(nums = [2,1,2,0,1,2,2,0]) == [0,0,1,1,2,2,2,2]
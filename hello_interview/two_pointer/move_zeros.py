class Solution:
    def moveZeroes(self, nums: list[int]):
        zeroindex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zeroindex], nums[i] = nums[i], nums[zeroindex]
                zeroindex += 1
        return nums
assert Solution().moveZeroes(nums = [2,0,4,0,9]) == [2,4,9,0,0]
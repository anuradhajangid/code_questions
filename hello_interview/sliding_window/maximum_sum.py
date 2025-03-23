class Solution:
    def maxSum(self, nums: list[int], k: int):
        moving_sum = 0
        start= 0
        max_sum = 0

        for i in range (len(nums)):
            moving_sum += nums[i]

            if i - start + 1 == k:
                max_sum = max(max_sum, moving_sum)
                moving_sum -= nums[start]
                start += 1

        return max_sum


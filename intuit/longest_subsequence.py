from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums-1,-1,-1)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)

import bisect
class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for i in range(len(nums)):
            lb  = bisect.bisect_left(lis, nums[i])
            if lb == len(lis):
                lis.append(lb)
            else:
                lis[lb] = nums[i]

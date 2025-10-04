#https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def backtrack(i):
            if i == len(nums):
                for m in range(k):
                    if result[i] != subset_sum:
                        return False
                return True
            for j in range(k):
                if result[j] + nums[i] <=subset_sum:
                    result[j] += nums[i]
                    if backtrack(j+1):
                        return True
                    result[j] -= nums[i]
            return False



        totalsum = sum(nums)
        maxelement = max(nums)
        subset_sum = totalsum/k
        if k > len(nums):
            return False
        if maxelement > totalsum/k:
            return False
        if int(totalsum/k) * k != totalsum:
            return False
        result = [0] * k
        nums = sorted(nums)
        backtrack(0)
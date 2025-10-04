#https://leetcode.com/problems/subarray-sum-equals-k/solutions/127728/subarray-sum-equals-k/?envType=problem-list-v2&envId=7p59281
from typing import List
from collections import defaultdict
class Solution:
    # with negative numbers, return count, O(N) TC, O(N) SC
    def subarraySum1(self, nums: List[int], k: int) -> int:
        sum_freq = defaultdict()
        sum_freq[0] = 1
        sum = 0
        count = 0
        for num in nums:
            sum += num
            complement = sum - k
            if complement in sum_freq:
                count += sum_freq[complement]
            if sum in sum_freq :
                sum_freq[sum] += 1
            else:
                sum_freq[sum] = 1
        return count
    # with negative numbers, return bool, O(N) TC, O(1) SC
    def subarraySum1(self, nums: List[int], k: int) -> int:
        sum_freq = set()
        sum_freq.add(0)
        sum = 0
        count = 0
        for num in nums:
            sum += num
            complement = sum - k
            if complement in sum_freq:
                return True
            sum_freq.add(sum)
        return False
    
    # with +ve numbers, return count, O(N) TC, O(1) SC
    def subarraySum1(self, nums: List[int], k: int) -> int:
        l = 0, r = 0
        count = 0
        sum = 0
        while r < len(nums):
            sum += nums[r]
            while (sum > k):
                sum -= nums[l]
                l += 1
            if sum == k:
                return True
        return False
    
assert Solution().subarraySum1(nums = [1, 2, 3], k = 3) == 2
        


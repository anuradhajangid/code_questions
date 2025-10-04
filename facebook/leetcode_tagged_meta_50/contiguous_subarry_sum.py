#https://leetcode.com/problems/continuous-subarray-sum/solutions/5259908/continuous-subarray-sum/?envType=problem-list-v2&envId=7p59281
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modmap = dict()
        modmap[0] = -1
        prefix_mod = 0
        for index, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % k
            if prefix_mod in modmap and index - modmap[prefix_mod] >= 2:
                return True
            modmap[prefix_mod] = index
        return False

        
assert Solution().checkSubarraySum(nums = [23,2,4,6,7], k = 6) == True
assert Solution().checkSubarraySum(nums = [23,2,6,4,7], k = 6) == True

        
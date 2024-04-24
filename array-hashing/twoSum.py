from typing import List
from collections import Counter
class Solution:
    def twoSum_approach1(self, nums: List[int], target: int) -> List[int]:
        # Runtime O(N**2), mem = 0
        self.len = len(nums)
        for i in range(self.len):
            for j in range (self.len):
                if nums[i]+nums[j] == target and i != j:
                    return [i,j]
    
    def twoSum_approach2(self, nums: List[int], target: int) -> List[int]:
        #Runtime O(N), additional memory = len*int = constant
        map = {}
        find = 0
        for i in range(len(nums)):
            find += nums[i]
            diff = target - nums[i]
            if diff in map:
                return [map[diff], i]
            map[nums[i]] = i
            find = 0
        
                
assert Solution().twoSum_approach1(nums = [2,7,11,15], target = 9) == [0,1]
assert Solution().twoSum_approach1(nums = [3,2,4], target = 6) == [1,2]
assert Solution().twoSum_approach1(nums = [3,3], target = 6) == [0,1]

assert Solution().twoSum_approach2(nums = [2,7,11,15], target = 9) == [0,1]
assert Solution().twoSum_approach2(nums = [3,2,4], target = 6) == [1,2]
assert Solution().twoSum_approach2(nums = [3,3], target = 6) == [0,1]
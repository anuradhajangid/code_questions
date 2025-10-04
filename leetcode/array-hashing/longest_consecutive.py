from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove duplicate & create a set hash table
        test = set(nums)
        maxlength = 0
        for num in test:
            if not (num-1 in test):
                length = 1
                while num+length in test:
                    length +=1
                if maxlength < length:
                    maxlength = length
        return maxlength
    
assert Solution().longestConsecutive([100,4,200,1,3,2]) == 4
assert Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]) ==9
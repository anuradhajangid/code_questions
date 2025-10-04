#https://leetcode.com/problems/find-unique-binary-string/
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        missing = []
        Solution.backtrack(missing, "", nums, len(nums[0]))
        return missing[0]

    @staticmethod
    def backtrack(missing: List, current: str, nums: List, n: int)->None:
        if len(current) == n:
            if current in nums:
                return 
            missing.append(current)
            return 
        for binary in ["0", "1"]:
            Solution.backtrack(missing, current + binary, nums, n)
            #Optimization to return first missing string
            if missing:
                return


assert Solution().findDifferentBinaryString(nums = ["01","10"]) in ["11", "00"]
assert Solution().findDifferentBinaryString(nums = ["00","01"]) in ["11", "10"]
assert Solution().findDifferentBinaryString(nums = ["111","011","001"]) in ["101", "000", "010", "100", "110"]
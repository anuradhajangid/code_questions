#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
from typing import List
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxlen = [0]
        Solution.backtrack(maxlen, "", 0, arr)
        return maxlen[0]

    @staticmethod
    def backtrack(maxlen, base,  index, arr):
        if maxlen[0] < len(base):
            maxlen[0] = len(base)
        for i in range(index, len(arr)):
            if not Solution.isValid(base, arr[i]):
                continue
            Solution.backtrack(maxlen, base+arr[i], i+1, arr)
            
    
    @staticmethod
    def isValid(basestring, addstring) -> bool:
        check = set()
        for char in addstring:
            if char in check:
                return False
            check.add(char)
            if char in basestring:
                return False
        return True

assert Solution().maxLength(arr = ["un","iq","ue"]) == 4
assert Solution().maxLength(arr = ["cha","r","act","ers"]) == 6
assert Solution().maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]) == 26
#https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/
class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0,len(s) -1
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while left <= right and s[right] == char:
                right -= 1
            
        return right - left + 1

        
assert Solution().minimumLength("ca") ==2
assert Solution().minimumLength("cabaabac") == 0
assert Solution().minimumLength("aabccabba") == 3

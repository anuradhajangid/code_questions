#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        maxlength = 1 if len(s) > 0 else 0
        for char in s[1:]:
            end += 1
            if char not in s[start:end]:
                maxlength = max(maxlength, len(s[start: end+1]))
            else:
                for visitedchar in s[start:end]:
                    start += 1
                    if char == visitedchar:
                        break
        return maxlength
        
#https://leetcode.com/problems/valid-palindrome-ii/description/?envType=problem-list-v2&envId=7p59281
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        while left < right:
            if s[left] != s[right]:
                return Solution._is_palindrom(left+1,right, s) or Solution._is_palindrom(left, right -1 ,s)
            left += 1
            right -= 1
        return True
    
    @staticmethod
    def _is_palindrom(i,j,s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
                
assert Solution().validPalindrome(s =
"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") == True
assert Solution().validPalindrome("cbbcc") == True
assert Solution().validPalindrome(s = "aba") == True
assert Solution().validPalindrome(s = "abca") == True
assert Solution().validPalindrome(s = "abc") == False
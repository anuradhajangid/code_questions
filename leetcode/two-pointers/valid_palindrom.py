import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) -1
        asciiChars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        palindromChar = None
        while (start < end):
            if not (s[start] in asciiChars):
                start += 1
                continue
            palindromChar = s[start]
            if not (s[end] in asciiChars):
                end -= 1
                continue
            if s[end].lower() == palindromChar.lower():
                start += 1
                end -= 1
            else:
                return False
        return True
    
    def isPalindrome_approach2(self, s: str) -> bool:
        s = s.strip().lower()
        if not s:
            return True
        s = "".join([i for i in s if i.isalnum()])
        return s == s[::-1]


assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
assert Solution().isPalindrome("race a car") == False
assert Solution().isPalindrome(" ") == True
assert Solution().isPalindrome_approach2("A man, a plan, a canal: Panama") == True
assert Solution().isPalindrome_approach2("race a car") == False
assert Solution().isPalindrome_approach2(" ") == True





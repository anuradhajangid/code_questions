import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) -1
        asciiChars = string.ascii_lowercase + string.ascii_uppercase + string.digits
        palindromChar = None
        while (start < end):
            print(start, end)
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





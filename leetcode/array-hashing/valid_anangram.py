from collections import Counter
class Solution(object):
    def isAnagram_approach1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
    def isAnagram_approach2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sdict = dict.fromkeys(s,0)
        i = 0
        while i < len(s):
            sdict[s[i]] += 1
            try:                
                sdict[t[i]] -= 1
            except KeyError:
                return False
            i += 1
        return not any(sdict.values())

assert Solution().isAnagram_approach1("anagram", "nagaram") == True
assert Solution().isAnagram_approach1("rat", "car") == False

assert Solution().isAnagram_approach2("anagram", "nagaram") == True
assert Solution().isAnagram_approach2("rat", "car") == False
#https://leetcode.com/problems/custom-sort-string/description/?envType=problem-list-v2&envId=7p59281
import collections
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_map = collections.Counter(s)
        res = ""
        if not order or not s:
            return s
        for char in order:
            if char in char_map:
                res += char * char_map[char]
                del char_map[char]
        for key, value in char_map.items():
            res += key * value
        return res

assert Solution().customSortString(order = "cba", s = "abcd") == "cbad"

"""Examples:
order = "abc", s = "adbcraa"
char_map = {}
res = "" ->aaa ->aab -> aabc ->aabcd -> aabcdr

order = "", s = "adbcraa"

order = "abc", s= ""


"""

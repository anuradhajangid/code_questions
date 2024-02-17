#https://leetcode.com/problems/palindrome-partitioning/description/
import copy
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        def backtracking(index, current):
            if index >= len(s):
                result.append(copy.deepcopy(current))
                return 
            for i in range(index,len(s)):
                if isValidPalindrom(s, index, i):
                    current.append(s[index:i+1])
                    backtracking(i+1, current)
                    current.pop()


        def isValidPalindrom(string, start, end):
            while start != end and start < end:
                if string[start] != string[end]:
                    return False
                start += 1
                end -= 1
            return True
        backtracking(0,[])
        return result

s = Solution()
assert s.partition("aab") == [["a","a","b"],["aa","b"]]
assert s.partition("aabcdc") == [['a', 'a', 'b', 'c', 'd', 'c'], ['a', 'a', 'b', 'cdc'], ['aa', 'b', 'c', 'd', 'c'], ['aa', 'b', 'cdc']]
assert s.partition("a") == [["a"]]
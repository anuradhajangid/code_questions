from typing import List
class Solution:
    def wordBreakTopDown(self, s: str, wordDict: List[str]) -> bool:
        def helper(s:str, index, memo, wordDict):
            if index == len(s):
                return True
            if memo[index] != -1:
                return memo[index]
            ans = False
            for word in wordDict:
                if s.startswith(word, index):
                    ans = ans or helper(s, index + len(word), memo, wordDict)
            memo[index] = ans
            return ans

        memo = [-1] * (len(s) + 1)
        index = 0
        return helper(s, index, memo, wordDict)
    
    def wordBottomUp(self, s: str, wordDict: List[str]) -> bool:
        memo = [-1] * (len(s) + 1)
        memo[len(s)] = 1
        for i in range(len(s)-1, -1, -1):
            ans = False
            for word in wordDict:
                if s[i: i+len(word)] == word:
                    ans = ans or memo[i+len(word)]
            memo[i] = 1 if ans else 0
        return memo[0] == 1
            
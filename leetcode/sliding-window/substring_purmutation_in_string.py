#https://leetcode.com/problems/permutation-in-string/submissions/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sortedsub = sorted(s1)
        start = 0
        for end in range(len(s1)-1,len(s2)):
            if sortedsub == sorted(s2[start: end+1]):
                return True
            start += 1
        return False

        

#https://leetcode.com/problems/daily-temperatures/description/
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                ttemp, ttemp_index = stack.pop()
                sol[ttemp_index] = index - ttemp_index
            stack.append([temp, index])
        return sol





s = Solution()
s.dailyTemperatures([73,74,75,71,69,72,76,73])

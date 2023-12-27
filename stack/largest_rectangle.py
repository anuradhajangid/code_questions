#https://leetcode.com/problems/largest-rectangle-in-histogram/
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxhis = 0
        for bar in heights + [-1]:
            count = 0
            while stack and stack[-1][1] >= bar:
                index, height = stack.pop()
                count += index
                maxhis = max(maxhis, count * height)
            stack.append([count + 1, bar])
        return maxhis


heights = [2,1,5,6,2,3]
s = Solution()
assert s.largestRectangleArea(heights) == 10

        
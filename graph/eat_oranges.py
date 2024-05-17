#https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/description/
from collections import deque
class Solution:
    def minDays(self, n: int) -> int:
        visited = set()
        runningQ = deque()
        days = 0
        runningQ.append((n, days))
        while runningQ:
            value, days = runningQ.popleft()
            if value == 0: return days
            visited.add(value)
            if value-1 not in visited: runningQ.append((value-1, days+1))
            if value%2 == 0 and value//2 not in visited: runningQ.append((value//2, days+1))
            if value%3 ==0 and value//3 not in visited: runningQ.append((value//3, days+1))
        return -1

assert Solution().minDays(10) == 4
assert Solution().minDays(6) == 3

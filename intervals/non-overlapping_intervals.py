from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        intervals = sorted(intervals, key=lambda x: x[1])
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev[1]:
                count +=1
            else:
                prev = intervals[i]
        return count

s = Solution()
assert s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
assert s.eraseOverlapIntervals([[1,2],[2,3]]) == 0

#TC: O(N)
#SP: O(1)

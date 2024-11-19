from typing import List
import heapq
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        previous = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] < previous[1]:
                return False
            previous = intervals[i]
        return True

s= Solution()
assert s.canAttendMeetings([[0,30],[5,10],[15,20]]) == False
assert s.canAttendMeetings([[7,10],[2,4]]) == True
assert s.canAttendMeetings([[0,30],[60,240],[90,120]]) == False
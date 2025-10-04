from typing import List
import heapq
class Solution:
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        result = [[intervals[0]]]
        for j in range(1, len(intervals)):
            found = False
            for i in range(0, len(result)):
                if intervals[j][0] < result[i][-1][1]:
                    continue
                else:
                    result[i].append(intervals[j])
                    found = True
                if found:
                    break
            if not found:
                result.append([intervals[j]])
        return len(result)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        mystack = []
        intervals = sorted(intervals, key = lambda x: x[0])
        for interval in intervals:
            if not mystack or interval[0] < mystack[0]:
                heapq.heappush(mystack, interval[1])
            else:
                heapq.heappop(mystack)
                heapq.heappush(mystack, interval[1])
        return len(mystack)

s= Solution()
assert s.minMeetingRooms([[1,5],[3,7],[4,6]]) == 3
assert s.minMeetingRooms([[1,5],[4,6],[6,8],[11,15]]) ==2
assert s.minMeetingRooms([[7,10],[2,4]]) == 1
assert s.minMeetingRooms([[1293,2986],[848,3846],[4284,5907],[4466,4781],[518,2918],[300,5870]]) == 4
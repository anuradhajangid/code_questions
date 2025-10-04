from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        i = 0
        res = []
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        if i < len(intervals):
            res.extend(intervals[i:len(intervals)])
        return res
            
s = Solution()
assert s.insert([[1,5]], [0,3]) == [[0,5]]
assert s.insert([[1,5]], [6,8]) == [[1,5],[6,8]]
assert s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]) == [[1,5],[6,9]]
assert s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]) == [[1,2],[3,10],[12,16]]

#TC: O(N)
#SC: O(N)
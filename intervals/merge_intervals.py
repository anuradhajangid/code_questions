from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key=lambda x: x[0])
        res = []
        for interval in  intervals:
            if res and interval[0] <=res[-1][1]:
                res[-1][1] = max(res[-1][1],interval[1])
            else:
                res.append(interval)
        return res
s = Solution()
assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
assert s.merge([[1,4],[4,5]]) == [[1,5]]

#TC: O(N) + O(nlogN) = O(NlogN)
#SP: O(N) worstcase, O(1), bestcase

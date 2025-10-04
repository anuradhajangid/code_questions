from typing import List

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        for index,range in enumerate(ranges):
            ranges[index] = [max(0,index-range), min(n, index+range)]
        ranges.sort(key=lambda x : x[0])
        memoize = {}

        def dynamicProgram(index, maxEnd):
            if index >= n+1:
                if maxEnd >= n:
                    return 0
                else:
                    return float("inf")
            if (index, maxEnd) in memoize:
                return memoize[(index, maxEnd)]
            if ranges[index][0] > maxEnd:
                return float("inf")
            open_tap =  1 + dynamicProgram(index + 1, max(maxEnd, ranges[index][1])) 
            close_tap = dynamicProgram(index+1, maxEnd)

            memoize[(index, maxEnd)]=min(open_tap, close_tap) 
            return memoize[(index, maxEnd)]
                
        result = dynamicProgram(0,0)
        return -1 if result == float("inf") else result
    


class Solution2:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n+1)
        for index,item in enumerate(ranges):
            s = max(0,index-item)
            e = min(n, index+item)
            arr[s] = max(arr[s],e)
        
        current = 0
        maxend = 0
        taps = 0

        for index in range(n+1):
            if index > maxend:
                return -1
            if index > current:
                current = maxend
                taps += 1
            maxend = max(maxend, arr[index])
        return taps

assert Solution2().minTaps(7, [1,2,1,0,2,1,0,1]) == 3

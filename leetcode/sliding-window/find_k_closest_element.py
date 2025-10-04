#https://leetcode.com/problems/find-k-closest-elements/
from typing import List
class Solution:
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, 0
        pos = 0
        for element in arr:
            data = abs(element-x)
            pos += 1
            if end-start + 1 <= k:
                end += 1
            else:
                if data >= abs(arr[start]-x):
                    continue
                else:
                    start = pos-k
                    end = pos
        return arr[start:end]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start, end = 0, len(arr)-k
        while start < end:
            mid = (start+end)//2
            if (x -arr[mid]) > (arr[mid+k] - x):
                start = mid + 1
            else:
                end = mid
        return arr[start: start+k]

    
assert Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3) == [1,2,3,4]
assert Solution().findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1) == [1,2,3,4]
assert Solution().findClosestElements(arr = [0,0,1,2,3,3,4,7,7,8], k= 3, x= 5) == [3,3,4]

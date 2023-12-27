from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = ceil(sum(piles)/h)
        end = max(piles)
        while start < end:
            mid = (start + end) // 2
            time = 0
            for i in piles:
                time += ceil(i/mid)
                if time > h:
                    break
            if time <= h:
                end = mid
            else:
                start = mid+1
        return end
    def minEatingSpeedOPBF(self, piles: List[int], h: int) -> int:
        k = ceil(sum(piles)/h)
        while True:
            time = 0
            for i in piles:
                time += ceil(i/k)
                if time > h:
                    break
            if time <= h:
                return k
            k += 1
    def minEatingSpeedBF(self, piles: List[int], h: int) -> int:
        k = 1
        while True:
            time = 0
            for i in piles:
                time += ceil(i/k)
            if time > h:
                k +=1
            else:
                return k
            

s = Solution()
assert s.minEatingSpeed([3,6,7,11], 8) == 4
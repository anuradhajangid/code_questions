#https://leetcode.com/problems/ipo/description/
import heapq
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        maxHeap = []

        for i in range(len(capital)):
            heapq.heappush(minHeap, (profits[i], capital[i]))

        while k > 0:
            while minHeap and minHeap[0][1] <= w:
                t = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-t[0], t[1]))
            if not maxHeap:
                break
            p, c = heapq.heappop(maxHeap)
            w -= p
            k -= 1

        return w


                    


assert Solution().findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]) == 4
assert Solution().findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]) == 6
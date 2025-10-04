from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        stack = []
        for num, freq in frequency.items():
            if len(stack) > k:
                stack.pop()
            heapq.heappush(stack, (-freq, num))
        result = [item[1] for item in stack]
        return result[:k]  

assert Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2) == [1,2]

        

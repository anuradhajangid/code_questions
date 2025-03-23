import heapq
class Solution:
    def kClosest(self, nums: list[int], k: int, target: int):
        # Your code goes here
        kheap = []
        for element in nums:
            value = abs(target-element)
            heapq.heappush(kheap, (-value, element))
            if len(kheap) > k:
                heapq.heappop(kheap)
        return [i for _, i in kheap]
    
assert Solution().kClosest(nums = [-1, 0, 1, 4, 6],target = 1, k = 3) == [-1, 0, 1]
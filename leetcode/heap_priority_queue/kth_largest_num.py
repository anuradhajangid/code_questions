#https://leetcode.com/problems/kth-largest-element-in-a-stream/

from heapq import *

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.numbers = nums
        self.heap = []

        counter = 1
        for num in self.numbers:
            heappush(self.heap,num)
            if counter > self.k:
                heappop(self.heap)
            counter += 1
        

    def add(self, num):
        heappush(self.heap,num)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
        

s = KthLargest(3,[4,5,8,2])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))


        

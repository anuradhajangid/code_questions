from heapq import *
#https://leetcode.com/problems/find-median-from-data-stream/description/

class MedianFinder(object):

    def __init__(self):
        self.max_small_num = []
        self.min_large_num = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.max_small_num or -self.max_small_num[0] >= num:
            heappush(self.max_small_num, -num)
        else:
            heappush(self.min_large_num, num)
        if len(self.max_small_num) > len(self.min_large_num) + 1:
            heappush(self.min_large_num, -heappop(self.max_small_num))
        elif len(self.max_small_num) < len(self.min_large_num):
            heappush(self.max_small_num, -heappop(self.min_large_num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_large_num) == len(self.max_small_num):
            return (-self.max_small_num[0] + self.min_large_num[0])/2
        return (-self.max_small_num[0])/1.0
        


medianFinder = MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.addNum(2)    # arr = [1, 2]
assert medianFinder.findMedian() == 1.5 # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)   # arr[1, 2, 3]
assert medianFinder.findMedian() == 2.0 # return 2.0
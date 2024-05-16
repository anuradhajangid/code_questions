#https://leetcode.com/problems/car-pooling/
from typing import List
from heapq import *
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        check = [] #Space O(n)
        running_capacity = 0
        trips.sort(key = lambda tup: tup[1]) #O(nlogn)
        for trip in trips: #O(n)
            if trip[0] > capacity or running_capacity > capacity:
                return False
            if check:
                while check and check[0][0] <= trip[1]:
                    item = heappop(check)
                    running_capacity -= item[2]

            running_capacity += trip[0]
            if running_capacity > capacity:
                return False
            heappush(check, [trip[2], trip[1], trip[0]])
        return True



assert Solution().carPooling(trips = [[2,1,5],[3,3,7]], capacity = 4) == False
assert Solution().carPooling(trips = [[2,1,5],[3,3,7]], capacity = 5) == True   
assert Solution().carPooling(trips = [[2,1,5],[3,5,7]], capacity = 3) == True  
assert Solution().carPooling([[2,2,6],[2,4,7],[8,6,7]], 11) == True 
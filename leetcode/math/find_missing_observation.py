#https://leetcode.com/problems/find-missing-observations/description/
from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_m = sum(rolls)
        mn = len(rolls) + n
        distribution = mean *  mn - sum_m
        if distribution <= 0 or distribution < n or distribution/n > 6:
            return []
        if distribution % n  == 0:
            return [distribution // n ] * n
        else:
            k = distribution % n
            dist_array = [distribution // n] * n
            for i in range(k):
                dist_array[i] += 1
                
        return dist_array

assert Solution().missingRolls(rolls = [3,2,4,3], mean = 4, n = 2) == [6,6]
assert Solution().missingRolls(rolls = [1,5,6], mean = 3, n = 4) == [3,2,2,2]
assert Solution().missingRolls(rolls = [1,2,3,4], mean = 6, n = 4) == []  
assert Solution().missingRolls([3,5,3], 5, 3) == []   
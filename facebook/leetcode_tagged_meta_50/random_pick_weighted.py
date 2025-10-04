# https://leetcode.com/problems/random-pick-with-weight/description/?envType=problem-list-v2&envId=7p59281
import random
from typing import List
class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.prefix_sum = []
        for weight in self.weights:
            if self.prefix_sum:
                self.prefix_sum.append(self.prefix_sum[-1] + weight)
            else:
                self.prefix_sum.append(weight)

    def pickIndex(self, target_index) -> int:
        target_index = random.randint(1, self.prefix_sum[-1]) % self.prefix_sum[-1]
        left = 0
        right = len(self.prefix_sum) -1
        while left <= right:
            middle = left + (right - left)//2
            if target_index < self.prefix_sum[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return left

sol= Solution([1])
assert sol.pickIndex([]) == 0
sol = Solution([1,3])
assert sol.pickIndex([]) == 1
assert sol.pickIndex([]) in [1,0]
assert sol.pickIndex([]) in [1,0]
assert sol.pickIndex([]) in [1,0]
assert sol.pickIndex([]) in [1,0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


#Variant  is cities and population from meta interview questions
class Solution:

    def __init__(self, data: List[(str, int)]):
        self.data = data
        self.prefix_sum = []
        for city, pop in self.data:
            if self.prefix_sum:
                self.prefix_sum.append((city, self.prefix_sum[-1] + pop))
            else:
                self.prefix_sum.append(pop)

    def pickIndex(self) -> int:
        target_index = random.randint(1, self.prefix_sum[-1][1]) % self.prefix_sum[-1][1]
        left = 0
        right = len(self.prefix_sum) -1
        while left <= right:
            middle = left + (right - left)//2
            if target_index < self.prefix_sum[middle][1]:
                right = middle - 1
            else:
                left = middle + 1
        return self.prefix_sum[left][0]
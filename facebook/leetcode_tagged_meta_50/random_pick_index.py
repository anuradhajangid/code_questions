#https://leetcode.com/problems/random-pick-index/?envType=problem-list-v2&envId=7p59281
from collections import defaultdict
import random
from typing import List

#Time complexity O(N), space complexity O(N), pick O(1)
class Solution:

    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        for index, num in enumerate(nums):
            self.map[num].append(index)
        

    def pick(self, target: int) -> int:
        return random.choice(self.map[target])

#Time complexity O(N), space complexity O(1), pick K numbers in O(N) time complexity and no extra space
class Solution2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def pick(self, k: int) -> int:
        pick_indices = []
        for i in range(k):
            pick_indices.append(self.nums[i])
        for i in range(k, len(self.nums)):
            index = random.randint(0,i) % i+1
            if index < k:
                pick_indices[index] = self.nums[i]
        return pick_indices

#Time complexity O(N), space complexity O(1), pick the index of max numbers from the array in O(N) time complexity and no extra space
class Solution2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def pick(self, k: int) -> int:
        max_number = - float("inf")
        picked_index = -1
        counter = 0
        for index, num in enumerate(self.nums):
            if num > max_number:
                max_number = num
                counter = 1
                picked_index = index
            elif num == max_number:
                counter += 1
                temp_index = random.random(counter) % counter
                if temp_index == 0:
                    picked_index = index
        return picked_index
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
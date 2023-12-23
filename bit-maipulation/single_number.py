from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        item = 0
        for num in nums:
            item = item ^ num
        return item

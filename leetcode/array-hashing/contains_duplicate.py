from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False

assert Solution().containsDuplicate([1,2,3,1]) == True
assert Solution().containsDuplicate([1,2,3,4]) == False
assert Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True

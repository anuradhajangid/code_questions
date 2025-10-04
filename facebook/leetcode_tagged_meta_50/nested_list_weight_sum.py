#https://leetcode.com/problems/nested-list-weight-sum/description/?envType=problem-list-v2&envId=7p59281
class Solution:
    def nestedListWeightSum(numbers:list):
        level = 1
        def helper(nums:list, level):
            sum = 0
            for element in nums:
                if isinstance(element, list):
                    sum += helper(element, level + 1)
                else:
                    sum += level * element
            return sum
        
        return helper(numbers, level)

from typing import List
class NestedList:
    def __init__(self):
        self.value: List['NestedList' | int]

class Solution:
    def nestedListWeightSum(numbers:NestedList):
        level = 1
        def helper(nums:NestedList, level):
            sum = 0
            for element in nums:
                if not isinstance(element, int):
                    sum += helper(element, level + 1)
                else:
                    sum += level * element
            return sum
        
        return helper(numbers, level)
    
from typing import List
from collections import deque
class Solution:
    def nestedListWeightSum(numbers:NestedList):
        queue = deque()
        sum = 0
        queue.append((numbers, 1))
        while queue:
            element, level = queue.popleft()
            for num in element:
                if not isinstance(element, int):
                    queue.append((num, level + 1))
                else:
                    sum += level * num
        return sum

""""
Examples
1. [1,2,[3,4,[]],5,[1,[0,[1]]]] = 1 + 2 + 2*3 + 2*4 + 2*0 + 5 + 2*1 + 3*0 + 4*1
2. []


"""  
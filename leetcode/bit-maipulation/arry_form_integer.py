#https://neetcode.io/practice
from typing import List
from collections import deque
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        end = len(num)-1
        result = deque()
        while k or end >= 0:
            if k:
                carry += k%10
                k = k//10
            if end >= 0:
                carry += num[end]
                end -= 1
            result.appendleft(carry%10)
            carry = carry // 10
        if carry:
            result.appendleft(carry)
        return list(result)

assert Solution().addToArrayForm(num = [1,2,0,0], k = 34) == [1,2,3,4]
assert Solution().addToArrayForm(num = [2,7,4], k = 181) == [4,5,5]
assert Solution().addToArrayForm(num = [2,1,5], k = 806) == [1,0,2,1]




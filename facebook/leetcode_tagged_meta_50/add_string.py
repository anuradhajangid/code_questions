from collections import deque
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pl = len(num1)
        ql = len(num2)
        n = max(pl, ql)
        res = deque()
        carry = 0
        for i in (range(n)):
            sum = carry + (int(num1[pl-i-1]) if i < pl else 0) + (int(num2[ql-i-1]) if i < ql else 0)   
            res.appendleft(str(sum%10))
            carry = sum//10
        if carry:
            res.appendleft(str(carry))
        return "".join(res)

assert Solution().addStrings("11", "123") == "134"
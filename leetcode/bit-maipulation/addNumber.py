#https://leetcode.com/problems/add-binary/description/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0 
        add = ""
        la = len(a) - 1
        lb = len(b) -1 
        while la >= 0 or lb >= 0:
            if la >= 0:
                carry += int(a[la])
                la -= 1
            if lb >= 0:
                carry += int(b[lb])
                lb -= 1
            add = str(carry%2) + add
            carry = int(carry/2)
        if carry:
            add = str(carry) + add
        return add

assert Solution().addBinary(a = "11", b = "1") == "100"
assert Solution().addBinary(a = "1010", b = "1011") == "10101"

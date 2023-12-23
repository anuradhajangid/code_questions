#https://leetcode.com/problems/multiply-strings/description/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n1 = 0
        for i in num1:
            n1 = n1*10 + (ord(i)- ord('0'))
        n2 = 0
        for i in num2:
            n2 = n2*10 + (ord(i)- ord('0'))
        
        ans = n1*n2
        ms = ''
        while ans:
            ms = chr(ord('0') + ans%10) + ms
            ans = ans // 10
        return ms

        
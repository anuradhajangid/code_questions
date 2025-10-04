#https://leetcode.com/problems/powx-n/description/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(n, p):
            if p==0 or n==1: return 1
            if p<0: return 1/calculate(n, -p)
            rs = calculate(n*n, p//2)
            return rs * n if p&1 else rs
        return calculate(x, n)

    def myPow1(self, x: float, n: int) -> float:
        if x==0 or n==1: return 1
        if n > 0:
            return self.calculatePow(x,n)
        else:
            return self.calculatePow(1/x, abs(n))

    def calculatePow(self, x, n):
        sum = x
        for i in range(1,n):
            sum *= x
        return sum
#https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        loop = set()
        while True:
            if n in loop:
                return False
            loop.add(n)
            if n == 1:
                return True
            sum = 0
            while n > 0:
                d = n%10
                sum += d*d
                n = int(n/10)
            n = sum
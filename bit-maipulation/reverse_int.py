#https://leetcode.com/problems/reverse-integer/description/
class Solution:
    max = 2**31-1
    min = -2**31
    def reverse(self, x: int) -> int:
        output = 0
        neg = False
        if x < 0:
            neg = True
        x= abs(x)
        while(x != 0):
            digit = x%10
            x = x//10

            if (output > self.max//10 and digit > x%10) or (output < self.min//10 and digit < x%10):
                return 0

            output = 10* output + digit

        if neg:
            output = -output
        return output

            


        
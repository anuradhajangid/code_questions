#https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits) -1:
                number = digits[i] + 1 + carry
            else:
                number = digits[i] + carry
            carry = int(number /10)
            digits[i] = number%10
        if not carry == 0:
            output = [carry]
            output.extend(digits)
            return output
        return digits
        
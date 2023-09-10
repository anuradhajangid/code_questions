class Solution:
    def reverseBits_2(self, n: int) -> int:
        output = 1 if n & 2147483648 == 2147483648 else 0
        n = n << 1
        for i in range (1, 32):
            temp = n & 2147483648
            if temp == 2147483648:
                output += (2**i)
            n = n << 1
        return output

    def reverseBits(self, n: int) -> int:
        output = 0
        for _ in range (31):
            output += n%2
            output <<= 1
            n >>= 1
        return output + n
        
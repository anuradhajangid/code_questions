class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while (n != 0):
            count = count + (n % 2)
            n = int(n/2)
        return count
    
    def hammingWeight_2(self, n: int) -> int:
        count = 0
        while(n > 0):
            count += n%2
            n = n >> 1
        return count

#https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        output = 0
        
        for i in range(len(arr)):
            val = arr[i]
            
            for k in range(i + 1, len(arr)):
                val ^= arr[k]
                
                if val == 0:
                    output += (k - i)
        
        return output

assert Solution().countTriplets([2,3,1,6,7]) == 4
assert Solution().countTriplets([1,1,1,1,1]) == 10
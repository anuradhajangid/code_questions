import math
from typing import List
class Solution:
    def productExceptSelf_approach1(self, nums: List[int]) -> List[int]:
        arraylen = len(nums)
        pre = 1
        post = 1
        i=1
        j=arraylen-2
        output = [1] * arraylen
        while i < arraylen and j >= 0: 
            pre = nums[i-1] * pre
            post = post * nums[j+1]
            output[i] *= pre
            output[j] *= post
            i += 1
            j -= 1

        i=0
        return output
    def productExceptSelf_approach2(self, nums: List[int]) -> List[int]:
        arraylen = len(nums)
        pre = [1] * arraylen
        post = [1] * arraylen
        for i in range(1, arraylen):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(arraylen-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        return [pre[i]*post[i] for i in range(arraylen)]

    def productExceptSelf_approach3(self, nums:List[int]) -> List[int]:
        arraylen = len(nums)
        pre = [1] * arraylen
        for i in range(1, arraylen):
            pre[i] = pre[i-1] * nums[i-1]
        post = 1
        for i in range(arraylen-2, -1, -1):
            post *= nums[i+1]
            pre[i] *= post
        return pre


assert Solution().productExceptSelf_approach1([1,2,3,4]) == [24,12,8,6]
assert Solution().productExceptSelf_approach1([-1,1,0,-3,3]) == [0,0,9,0,0]

assert Solution().productExceptSelf_approach2([1,2,3,4]) == [24,12,8,6]
assert Solution().productExceptSelf_approach2([-1,1,0,-3,3]) == [0,0,9,0,0] 
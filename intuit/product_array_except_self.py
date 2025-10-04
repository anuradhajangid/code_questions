from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp_product_forward = [1] * (len(nums))
        temp_product_backwards = [1] * (len(nums))
        for i in range(1, len(nums)):
            temp_product_forward[i] = temp_product_forward[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            temp_product_backwards[i] = temp_product_forward[i+1] * nums[i+1]
        for i in range(len(nums)):
            temp_product_forward[i] = temp_product_forward[i] * temp_product_backwards[i]
        return temp_product_forward
    
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp_product_forward = [1] * (len(nums))
        for i in range(1, len(nums)):
            temp_product_forward[i] = temp_product_forward[i-1] * nums[i-1]
        post = 1
        for i in range(len(nums)-2, -1, -1):
            post *= nums[i+1]
            temp_product_forward[i] *= post
        return temp_product_forward
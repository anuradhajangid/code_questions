from typing import List
class Solution:
    def mergeSort(self, nums: List):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)


    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[i])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

            
print (Solution().mergeSort([3, 7, 6, -10, 15, 23.5, 55, -13]))

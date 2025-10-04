# https://leetcode.com/problems/split-array-largest-sum/

from typing import List

class Solution:
    def splitArray_2(self, nums: List[int], k: int) -> int:
        dp = {}

        def dfs (i, m):
            if m == 1:
                return sum(nums[i:])
            if (i, m) in dp:
                return dp[(i,m)]
            res, csum =float("inf"), 0
            for j in range(i, len(nums) -m +1):
                csum += nums[j]
                maxsum = max(csum, dfs(j+1, m-1))
                res = min(res, maxsum)
                if csum > res:
                    break
            dp[(i,m)] = res
            return res
        return dfs(0,k)

    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        result = right
        def isSplitPossible(largest):
            subarray = 0
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > largest:
                    subarray += 1
                    currSum = n
            return subarray + 1 <= k


        while left <= right:
            mid = left + (right-left)//2
            if isSplitPossible(mid):
                result = mid
                right = mid -1
            else:
                left = mid +1
        return result

        
    
assert Solution().splitArray(nums = [7,2,5,10,8], k = 2) == 18
assert Solution().splitArray(nums = [1,2,3,4,5], k = 2) == 9
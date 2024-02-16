#https://leetcode.com/problems/subsets-ii/
class Solution(object):
    def subsetsWithDupLessOptimized(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        def backtrack(indexednums, current, result):
            if not current in result:
                result.append(current)
            for i in range(len(indexednums)):
                backtrack(indexednums[i+1:], current+[indexednums[i]], result)
        backtrack(nums, [], result)
        return result
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)
        def backtrack(index, current):
            result.append(list(current))
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
        backtrack(0, [])
        return result

s = Solution()
#[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert s.subsetsWithDup([1,2,2]) == [[],[1],[1,2],[1,2,2],[2],[2,2]]
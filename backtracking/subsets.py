#https://leetcode.com/problems/subsets/description/
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(indexednums, current, result):
            result.append(current)
            for i in range(len(indexednums)):
                backtrack(indexednums[i+1:], current+[indexednums[i]], result)
        backtrack(nums, [], result)
        return result
    
s = Solution()
print(s.subsets([1,2,3]))
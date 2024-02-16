#https://leetcode.com/problems/subsets-ii/

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(indexednums, current, result):
            if not current in result:
                result.append(current)
            for i in range(len(indexednums)):
                backtrack(indexednums[i+1:], current+[indexednums[i]], result)
        backtrack(nums, [], result)
        return result

s = Solution()
#[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert s.subsetsWithDup([1,2,2]) == [[],[1],[1,2],[1,2,2],[2],[2,2]]
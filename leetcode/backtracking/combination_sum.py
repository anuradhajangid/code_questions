#https://leetcode.com/problems/combination-sum/
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(candidates, target, [], result)
        return result
    
    def backtrack(self, nums, target, path, result):
        if target < 0:
            return 
        if target == 0:
            result.append(path)
            return 
        for i in range(len(nums)):
            self.backtrack(nums[i:], target-nums[i], path+[nums[i]], result)
        

        


s = Solution()
assert s.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]
#https://leetcode.com/problems/combination-sum/
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(candidates)
        self.backtrack(0,candidates, target, [], result)
        return result
    
    def backtrack(self, index, nums, target, path, result):
        if target < 0:
            return 
        if target == 0:
            result.append(path)
            return 
        prev = -1
        for i in range(index,len(nums)):
            if nums[i] == prev:
                continue
            self.backtrack(i+1, nums, target-nums[i], path+[nums[i]], result)
            prev = nums[i]
            
        

        


s = Solution()
assert s.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]]
assert s.combinationSum2([2,5,2,1,2], 5) == [[1,2,2],[5]]
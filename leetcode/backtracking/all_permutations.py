#https://leetcode.com/problems/permutations/
import copy
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        Solution._backtrack(nums, result, [])
        return result
    
    @staticmethod
    def _backtrack(nums, result, path):
        if len(path) == len(nums):
            result.append(path)
            #result.append(copy.deepcopy(path))
            return
        for num in nums:
            if num not in path:
                #path.append(num)
                #Solution._backtrack(nums, result, path)
                Solution._backtrack(nums, result, path+[num])
                #path.pop()


        

s = Solution()
assert s.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
assert s.permute([0,1]) == [[0,1],[1,0]]
assert s.permute([1]) == [[1]]
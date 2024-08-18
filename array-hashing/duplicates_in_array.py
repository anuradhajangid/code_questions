#https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        repeated_nums = []
        for item in nums:
            abs_item = abs(item)
            position = abs_item -1
            if nums[position] < 0:
                repeated_nums.append(abs(item))
            else:
                nums[position] = -nums[position]
        return repeated_nums


assert Solution().findDuplicates([4,3,2,7,8,2,3,1]) == [2,3]
assert Solution().findDuplicates([1,1,2]) == [1]
assert Solution().findDuplicates([1]) == []
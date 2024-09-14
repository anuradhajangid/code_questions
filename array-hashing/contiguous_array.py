class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeroCount = 0
        oneCount = 0
        maxLength = 0
        diffMap  = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else: oneCount += 1
            diff = zeroCount - oneCount 
            if diff in diffMap:
                maxLength = max(maxLength, i - diffMap[diff])
            else:
                diffMap[diff] = i
        return maxLength
assert Solution().findMaxLength([0,1]) ==2

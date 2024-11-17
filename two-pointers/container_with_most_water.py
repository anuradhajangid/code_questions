class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) -1
        maxWater = 0
        while left < right:
            minH = min(height[left], height[right])
            maxWater = max(maxWater, minH * (right - left))
            if height[left] < height [right]:
                left += 1
            else:
                right -= 1
        return maxWater
                
        
assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert Solution().maxArea([1,1]) == 1

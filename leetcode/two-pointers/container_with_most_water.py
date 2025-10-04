class Solution(object):
    def maxAreaBruteForce(self, height):
        maxarea = 0
        for i in range (len(height)):
            hl = height[i]
            for j in range(i+1, len(height)):
                hr = height[j]
                maxarea = max(maxarea, min(hr, hl) * (j-i))
        return maxarea
    
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

assert Solution().maxAreaBruteForce([1,8,6,2,5,4,8,3,7]) == 49
assert Solution().maxAreaBruteForce([1,1]) == 1             
        
assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert Solution().maxArea([1,1]) == 1

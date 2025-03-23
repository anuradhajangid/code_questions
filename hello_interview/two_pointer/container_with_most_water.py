class Solution:
    def max_area(self, heights):
        n = len(heights)
        left = 0
        right = n -1
        maxw = 0
        while left < right:
            if heights[right] >= heights[left]:
                maxw = max(maxw, heights[left] * (n-1))
                left += 1
            else:
                maxw = max(maxw, heights[right] * (n-1))
                right -= 1
            n -= 1
        return maxw



assert Solution().max_area(heights = [3,4,1,2,2,4,1,3,2]) == 21
assert Solution().max_area(heights = [1,2,1]) == 2


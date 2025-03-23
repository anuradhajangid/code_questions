class Solution:
    def trappingWater(self, height: list[int]):
        if not height:
            return 0
        left = 0
        right = len(height) -1
        leftMax = height[left]
        rightMax = height[right]
        water = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
        return water


assert Solution().trappingWater(height = [3, 4, 1, 2, 2, 5, 1, 0, 2]) == 10

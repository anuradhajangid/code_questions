class Solution():
    def largestHistogram(self, heights):
        hist_stack = [] # index, height
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while hist_stack and h < hist_stack[-1][1]:
                index, height = hist_stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            hist_stack.append((start, h))
        
        for i, h in hist_stack:
            maxArea = max(maxArea, h * (len(heights) - i ))
            hist_stack.pop()

        return maxArea

assert Solution().largestHistogram(heights = [2,8,5,6,2,3]) == 15



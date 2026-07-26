class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack=[]
        n = len(heights)
        max_h = 0
        for i in range(n+1):
            curr_h = 0 if i == n else heights[i]
            while stack and curr_h<heights[stack[-1]]:
                popped_idx = stack.pop()
                popped_bar_h = heights[popped_idx]
                right=i
                left=stack[-1] if stack else -1
                width = right-left-1
                area = popped_bar_h*width
                max_h = max(max_h,area)
            stack.append(i)
        return max_h


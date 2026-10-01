class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # find how much we can extend each bar by at a given index
        # so its not descending each way
        l_stack, r_stack = [], []
        left = [-1] * len(heights)
        right = [-1] * len(heights)
        # keep two stacks to track non descending orders in both directions of i
        for i in range(len(heights)):
            while l_stack and heights[l_stack[-1]] >= heights[i]:
                   l_stack.pop()
            
            if l_stack:
                left[i] = l_stack[-1]
            else:
                left[i] = -1

            l_stack.append(i)

        for i in range(len(heights) - 1, -1, -1):
            while r_stack and heights[r_stack[-1]] >= heights[i]:
                   r_stack.pop()
            
            if r_stack:
                right[i] = r_stack[-1]
            else:
                right[i] = len(heights)

            r_stack.append(i)
        
        ans = 0
        for i in range(len(heights)):
            area = (right[i] - left[i] - 1) * heights[i]
            ans = max(area, ans)

        return ans



        
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # could you have l and r?
        
        # move the smaller one and calculate area?
        ans = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            ans = max(ans, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return ans
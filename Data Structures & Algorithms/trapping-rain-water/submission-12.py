class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        max_left = [-1] * len(height)
        max_right = [-1] * len(height)

        hi = 0
        for i in range(len(height)):
            hi = max(hi, height[i])
            max_left[i] = hi

        hi = 0
        for i in range(len(height) - 1, -1, -1):
            hi = max(hi, height[i])
            max_right[i] = hi

        # print(height)
        # print(max_left)
        # print(max_right)

        ans = 0

        for i in range(len(height)):
            ans += min(max_left[i], max_right[i]) - height[i]
      
        return ans

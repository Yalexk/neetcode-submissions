class Solution:
    def rob(self, nums: List[int]) -> int:
        h = {}
        
        for i in range(len(nums)):
            oneBehind, twoBehind = h.get(i - 1, 0), h.get(i - 2, 0)
            h[i] = max(oneBehind, twoBehind + nums[i])

        return h[len(nums) - 1]
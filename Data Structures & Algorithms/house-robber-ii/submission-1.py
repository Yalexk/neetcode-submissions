class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(s): 
            s1, s2 = 0, 0 # s1, s2, n, n+1, ...
            if s == 0: 
                end = len(nums) - 1
            else:
                end = len(nums)

            for i in range(s, end):
                temp = max(nums[i] + s1, s2)
                s1 = s2
                s2 = temp
            
            return s2

        if len(nums) == 1:
            return nums[0]
            
        return max(dp(0), dp(1))
        
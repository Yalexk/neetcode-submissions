class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin, res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)): 
            cur = nums[i]  
            candidates = (cur, curMax * cur, curMin * cur)

            curMax = max(candidates)
            curMin = min(candidates)

            res = max(res, curMax)
        
        return res

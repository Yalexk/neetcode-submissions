class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # easy solution would be to go through and multiply all together
        # then divide by the current number on a second pass
        # is there a way to multiply them all EXCEPT?
        ans = [1] * len(nums)
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        total = 1
        for i in range(len(nums)):
            forward[i] = total
            total *= nums[i]
        
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            backward[i] = total
            total *= nums[i]
        
        # print(forward, backward)
        
        for i in range(len(nums)):
            ans[i] = forward[i] * backward[i]

        return ans
        

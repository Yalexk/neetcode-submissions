class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(len(nums)):
            target = -1 * nums[i]

            l = i + 1
            r = len(nums) - 1
            while l < r:
                n = nums[l] + nums[r]
                if n == target:
                    num = [nums[i], nums[l], nums[r]]
                    if num not in ans: ans.append(num)
                    r -= 1
                    l += 1
                elif n > target:
                    r -= 1
                elif n < target:
                    l += 1
        
        return ans
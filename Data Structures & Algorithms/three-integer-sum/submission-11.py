class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            target = -1 * nums[i]

            l = i + 1
            r = len(nums) - 1
            while l < r:
                n = nums[l] + nums[r]
                if n == target:
                    num = [nums[i], nums[l], nums[r]]
                    ans.append(num)

                    r_num = nums[r]
                    l_num = nums[l]

                    l += 1
                    r -= 1

                    while l < r and nums[l] == l_num:
                        l += 1

                elif n > target:
                    r -= 1
                elif n < target:
                    l += 1
        
        return ans
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, total, numbers):
            if total == target:
                self.res.append(numbers.copy())
                return
            
            if total > target or i >= len(nums):
                return
            
            numbers.append(nums[i])
            dfs(i, total + nums[i], numbers)
            numbers.pop()
            dfs(i + 1, total, numbers)

        dfs(0, 0, [])
        
        return self.res
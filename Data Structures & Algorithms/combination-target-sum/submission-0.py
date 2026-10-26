class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def recurse(i, summation, numbers):
            if summation == target:
                if numbers not in self.res:
                    self.res.append(numbers.copy())
                return
            
            if summation > target:
                return
            
            for j in range(i, len(nums)):
                numbers.append(nums[j])
                recurse(j, summation + nums[j], numbers)
                numbers.pop()

        recurse(0, 0, [])
        
        return self.res
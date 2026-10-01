class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            num = numbers[l] + numbers[r] 
            if num > target:
                r -= 1
            elif num < target:
                l += 1
            elif num == target:
                return [l + 1, r + 1]
        


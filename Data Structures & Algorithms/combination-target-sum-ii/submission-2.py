class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        
        def dfs(i, total, numbers):
            if total == target:
                res.append(numbers.copy())
                return
    
            if i >= len(candidates) or total > target:
                return

            numbers.append(candidates[i])
            dfs(i + 1, total + candidates[i], numbers)

            numbers.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            dfs(i + 1, total, numbers)
            
        
        dfs(0, 0, [])

        return res
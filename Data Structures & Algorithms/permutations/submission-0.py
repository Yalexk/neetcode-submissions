class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []

        def dfs(i, numbers):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            # preserve order by just creating a new list!
            for j in range(len(numbers)):
                cur.append(numbers[j])
                new_numbers = numbers[:j] + numbers[j+1:]
                dfs(i + 1, new_numbers)

                cur.pop()
        

        dfs(0, nums)

        return res
                
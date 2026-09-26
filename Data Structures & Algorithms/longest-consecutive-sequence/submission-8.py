class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # is there a way to identify the start of the sequence
        # do two passes and identify if a number has no number before it
        if not nums:
            return 0
        
        nums = set(nums)
        
        starts = []
        for num in nums:
            if num - 1 not in nums:
                starts.append(num)

        ans = 0
        for num in nums:
            if num in starts:
                curr = num
                count = 0
                while curr in nums:
                    curr += 1
                    count += 1
                ans = max(count, ans)
        return ans
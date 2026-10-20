class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = r = 0
        q = collections.deque() # index
        ans = []

        while r < len(nums):
            # pop smaller than current
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1
        
        return ans

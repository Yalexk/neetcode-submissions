class Solution:
    def climbStairs(self, n: int) -> int:
    
        if n <= 2:
            return n
        
        prev, prevprev = 2, 1
        
        cur = 0
        for i in range(3, n + 1):
            cur = prev + prevprev
            prevprev = prev
            prev = cur
        
        return cur
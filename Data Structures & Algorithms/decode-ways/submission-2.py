class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i >= len(s):
                return 1
            
            if i in memo.keys():
                return memo[i]

            
            cur = int(s[i])

            if cur in (1, 2) and i + 1 < len(s):
                nxt = int(s[i + 1])
                if cur == 1 or cur == 2 and nxt <= 6:
                    memo[i] = dfs(i + 1) + dfs(i + 2)
                    return memo[i]
            
            if cur == 0:
                memo[i] = 0
                return 0
            
            memo[i] = dfs(i + 1)
            return memo[i]
                    
        
        return dfs(0)
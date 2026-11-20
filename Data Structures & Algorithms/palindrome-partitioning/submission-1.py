class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substrings = [s[0]]


        # dynamic programming approach: precompute all possible palindromes
        # dp[i][j] == True, if s[i:j+1] is a palindrome
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if length == 1:
                    dp[l][r] = True
                elif length == 2:
                    dp[l][r] = s[l] == s[r]
                else:
                    dp[l][r] = s[l] == s[r] and dp[l+1][r-1] 

        def dfs(i, start):
            if i == len(s):
                if dp[start][i - 1]:
                    res.append(substrings.copy())
                return
            
            substrings[-1] += s[i]
            dfs(i + 1, start)

            substrings[-1] = substrings[-1][:-1]

            # only split if the current is a palindrome
            if dp[start][i - 1]:
                substrings.append(s[i])
                dfs(i + 1, i)
                substrings.pop()
            
            return


        dfs(1, 0)

        return res
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return (l + 1, r - 1)
        
        ans = ""
        for i in range(len(s)):
            l, r = expand(i - 1, i + 1)
            if (r - l + 1) > len(ans):
                ans = s[l:r+1]
            
            if i < len(s) - 1 and s[i] == s[i + 1]:
                l, r = expand(i - 1, i + 2)
                if (r - l + 1) > len(ans):
                    ans = s[l:r+1]
        
        return ans
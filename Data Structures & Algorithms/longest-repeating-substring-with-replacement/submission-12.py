class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the condition is that there are k+1 unique characters in teh string
        l = 0
        res = 0
        freqs = {}
        maxf = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            maxf = max(maxf, freqs[s[r]])       
            while (r - l + 1) - maxf > k:
                freqs[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res              
                    




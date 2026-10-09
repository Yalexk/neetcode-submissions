class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # the condition is that there are k+1 unique characters in teh string
        l = 0
        res = 0
        freqs = {}
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            # take the current substring and count number of character != most popular
            
            maxc = max(freqs, key=freqs.get)

            windowLength = r - l + 1            
            
            if windowLength - freqs[maxc] <= k:
                res = max(windowLength, res)
            else:
                while r - l + 1 - freqs[maxc] > k:
                    freqs[s[l]] = freqs.get(s[l]) - 1
                    maxc = max(freqs, key=freqs.get)
                    l += 1


        return res              
                    




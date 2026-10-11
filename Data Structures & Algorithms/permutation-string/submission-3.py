class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window of size s1, check each to see if it is a perm
        # if the current substring is invalid, expand until we find a character in s1
        # shrink for each we contract
        # we can maniuplate s1
        if len(s1) > len(s2):
            return False
            
        s1Freq, freqs = {}, {}

        for c in s1:
            s1Freq[c] = 1 + s1Freq.get(c, 0) 

        l = 0
        count = 0
        for r in range(0, len(s2)):
            if count < len(s1):
                freqs[s2[r]] = 1 + freqs.get(s2[r], 0)
                count += 1
            elif freqs == s1Freq:
                return True
            else:
                freqs[s2[r]] = 1 + freqs.get(s2[r], 0)
                freqs[s2[l]] -= 1
                if freqs[s2[l]] == 0: del freqs[s2[l]]
                l += 1
        
        if freqs == s1Freq:
            return True

        return False
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tFreq = {}
        for c in t:
            tFreq[c] = tFreq.get(c, 0) + 1

        freqs = {}
        formed = 0
        required = len(tFreq)

        l = 0
        res = ""
        minLen = float("inf")

        for r in range(len(s)):
            # Expand: add s[r] to the window
            c = s[r]
            freqs[c] = freqs.get(c, 0) + 1

            # Did this character just satisfy its requirement?
            if c in tFreq and freqs[c] == tFreq[c]:
                formed += 1

            # Shrink while all character requirements are satisfied
            while formed == required:
                windowLen = r - l + 1

                if windowLen < minLen:
                    minLen = windowLen
                    res = s[l:r + 1]

                # Remove s[l] from the window
                leftChar = s[l]

                if leftChar in tFreq and freqs[leftChar] == tFreq[leftChar]:
                    formed -= 1

                freqs[leftChar] -= 1
                l += 1

        return res
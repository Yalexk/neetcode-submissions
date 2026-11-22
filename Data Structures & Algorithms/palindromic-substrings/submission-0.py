class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n
        for i in range(n):
            # odd case
            l, r = i - 1, i + 1
            while l >= 0 and r < n:
                if s[r] == s[l]:
                    count += 1
                    l -= 1
                    r += 1
                else:
                    break

            # even case
            if i + 1 < n and s[i] == s[i + 1]:
                count += 1
                l, r = i - 1, i + 2
                while l >= 0 and r < n:
                    if s[r] == s[l]:
                        count += 1
                        l -= 1
                        r += 1
                    else:
                        break
        
        return count
            
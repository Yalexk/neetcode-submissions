class Solution:
    def isPalindrome(self, s: str) -> bool:
        # preprocess
        new_s = ''
        for char in s:
            if char.isalnum():
                new_s += char.lower()

        l = 0
        r = len(new_s) - 1

        while l < r:
            if new_s[l] != new_s[r]: return False
            l += 1
            r -= 1
        
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorth both strings then go character by char?
        # create two hash maps, they should be equal
        d1, d2 = {}, {}

        for c in s:
            count = d1.get(c)
            if not count: 
                d1[c] = 1
            else:
                d1[c] += 1
        for c in t:
            count = d2.get(c)
            if not count: 
                d2[c] = 1
            else:
                d2[c] += 1

        if d1 != d2:
            return False

        return True
    
        
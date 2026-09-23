class Solution:
    # keep track of some sort of spacing rule?
    def encode(self, strs: List[str]) -> str:
        # 5words4word
        enc_str = ""
        for string in strs:
            enc_str = enc_str + '%' + str(len(string)) + '%' + string
        print(enc_str)
        return enc_str

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s): 
            if s[i] == '%':
                length = ''
                i += 1
                while s[i] != '%':
                    length = length + s[i]
                    i += 1
                # print(length)
                length = int(length)
                # i is now at the second %
                ans.append(s[i + 1: i + 1 + length])
                i += 1 + length
            else: i += 1
              
        return ans
                
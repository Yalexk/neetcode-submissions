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
        ans = []
        i = 0
        start = -1
        end = 0
        while i < len(s):
            if s[i] == '%': 
                if start < end:
                    start = i
                    i += 1
                else:
                    end = i
                    # print(start, end)
                    # print(s[start + 1:end])
                    length = int(s[start + 1:end])
                    ans.append(s[end + 1: end + length + 1])
                    i += length + 1
            else: i += 1
              
        return ans
                
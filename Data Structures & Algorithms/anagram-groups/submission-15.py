class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each string
        # create an array for each string
        # array to index
        ans = []
        hmap = {}

        for s in strs:
            s_arr = [0] * 26
            for c in s:
                # print(ord(c))
                s_arr[ord(c) - 97] += 1

            s_arr = tuple(s_arr)
            if s_arr not in hmap:
                hmap[s_arr] = len(ans)
                ans.append([s])
            else:
                ans[hmap[s_arr]].append(s)

        return ans        
            

        
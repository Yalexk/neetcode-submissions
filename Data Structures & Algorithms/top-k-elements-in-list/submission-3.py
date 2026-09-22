class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freqs = {} # frequency hash which maps frequency -> numbers in an array
        for num in nums:
            count = hmap.get(num)
            if not count:
                hmap[num] = 1
                if not freqs.get(1):
                    freqs[1] = [num]
                else:
                    freqs[1].append(num)

            else:
                hmap[num] += 1
                if not freqs.get(hmap[num]):
                    freqs[hmap[num]] = [num]
                else:
                    freqs[hmap[num]].append(num)
        
        # print(hmap)
        # print(freqs)
        vals = list(reversed(freqs.values()))
        # print(vals)
        ans = []

        for val in vals:
            for num in val:
                if num not in ans:
                    ans.append(num)
                    k -= 1
                    if k == 0: return ans
         
        
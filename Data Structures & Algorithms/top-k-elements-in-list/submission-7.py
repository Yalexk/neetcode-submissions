class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freqs = [[] for _ in range(len(nums) + 2)] # map frequency to array index
        for num in nums:
            count = hmap.get(num)
            if not count:
                hmap[num] = 1
                freqs[1].append(num)

            else:
                hmap[num] += 1
                freqs[hmap[num]].append(num)
        
        # print(hmap)
        # print(freqs)
        ans = []
        i = len(nums)
        while i > 0 and k > 0:
            for num in freqs[i]:
                if num not in freqs[i + 1]:
                    k -= 1
                    ans.append(num)
            i -= 1
        
        return list(ans)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freqs = [[] for _ in range(len(nums) + 1)] # map frequency to array index
        for num in nums:
            count = hmap.get(num)
            if not count:
                hmap[num] = 1

            else:
                hmap[num] += 1

        for key, value in hmap.items():
            freqs[value].append(key)        
        # print(hmap)
        # print(freqs)

        ans = []
        for i in range(len(nums), 0, -1):
            for num in freqs[i]:
                ans.append(num)
                k -= 1
                if k == 0: return ans
    

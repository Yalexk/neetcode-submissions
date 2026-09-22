class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        freqs = [[] for _ in range(len(nums) + 1)] # map frequency to array index
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        for key, value in hmap.items():
            freqs[value].append(key)   
            

        ans = []
        for i in range(len(nums), 0, -1):
            for num in freqs[i]:
                ans.append(num)
                k -= 1
                if k == 0: return ans
    

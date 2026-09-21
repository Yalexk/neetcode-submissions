class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in hmap.keys():
                # return the indices
                return[hmap[num], i]
            hmap[target - num] = i

        
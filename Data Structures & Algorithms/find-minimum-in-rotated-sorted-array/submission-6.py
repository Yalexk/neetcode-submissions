class Solution:
    def findMin(self, nums: List[int]) -> int:
        # case 1 lo < hi
        # perform regular binary search since the segment is in order

        # case 2: lo > hi
        # middle is min: reverse
        # middle is larger: reverse
        lo, hi = 0, len(nums) - 1

        ans = float("inf")
        while lo < hi:
            mid = lo + ((hi - lo) // 2) 

            if nums[mid] < nums[hi]:
                hi = mid
            
            else:
                lo = mid + 1
        
        return nums[lo]


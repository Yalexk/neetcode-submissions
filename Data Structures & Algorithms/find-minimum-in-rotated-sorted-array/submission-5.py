class Solution:
    def findMin(self, nums: List[int]) -> int:
        # case 1 lo < hi
        # perform regular binary search since the segment is in order

        # case 2: lo > hi
        # middle is min: reverse
        # middle is larger: reverse
        lo, hi = 0, len(nums) - 1

        ans = float("inf")
        while lo <= hi:
            mid = lo + ((hi - lo) // 2) 

            if nums[lo] < nums[hi]:
                if nums[mid] < ans:
                    ans = min(ans, nums[mid])

                    hi = mid - 1
                else:
                    return ans
            
            else:
                # [2,3,4,0,1] # we go to the lower one if mid is higher than both
                # [4,0,1,2,3,] # if mid is lower than both we go to the higher one
                if nums[mid] >= nums[lo] and nums[mid] >= nums[hi]:
                    # middle is bigger than both so go towards the smaller one
                    if nums[mid] - nums[lo] > nums[mid] - nums[hi]:
                        hi = mid - 1
                    else:
                        lo = mid + 1              
                else:
                    # mid is smaller than both go toward bigger number
                    if nums[lo] - nums[mid] > nums[hi] - nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                ans = min(ans, nums[mid])

        
        return ans


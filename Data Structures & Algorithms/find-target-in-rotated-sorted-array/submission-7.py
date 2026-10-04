class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            print(l, m, r)

            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                # left half is sorted 
                # is target is left or right side
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1

            else: # nums[r] >= nums[m]:                 
                # right half is sorted
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        
        return -1

        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # go to the index of the current number
        # [4,1,4,3,2]
        slow, fast = 0, 0
        slow2 = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if nums[slow] == nums[fast]:
                break
        
        while True:
            if nums[slow2] == nums[slow]:
                return nums[slow]

            slow = nums[slow]
            slow2 = nums[slow2]

           
            
            
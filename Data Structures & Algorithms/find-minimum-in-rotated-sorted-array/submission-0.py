class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        # no rotation case
        if nums[l] < nums[r]:
            return nums[l]
        
        # nums[l] > nums[r] always

        while l <= r:
            m = l + ((r - l) // 2)
            if r - l <= 1:
                return min(nums[l], nums[r])
             
            if nums[l] < nums[m]:
                l = m
            elif nums[m] < nums[r]:
                r = m
        
        return 0
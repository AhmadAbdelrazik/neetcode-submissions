class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        for i in range(len(nums)):
            j = len(nums) - i - 1
            if i == 0:
                left[i] = nums[i]
                right[j] = nums[j]
                continue
            left[i] = nums[i]*left[i-1]
            right[j] = nums[j]*right[j+1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = right[1]
                continue
            
            if i == len(nums)-1:
                res[i] = left[i-1]
                continue
                
            res[i] = left[i-1] * right[i+1]
        
        return res


                
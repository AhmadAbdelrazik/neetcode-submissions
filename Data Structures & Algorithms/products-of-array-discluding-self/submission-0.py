class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        leftArr = [1 for x in nums]
        for i in range(len(nums)):
            if i == 0:
                leftArr[i] = nums[i]
            else:
                leftArr[i] = nums[i] * leftArr[i-1]

        rightArr = [1 for x in nums]
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                rightArr[i] = nums[i]
            else:
                rightArr[i] = nums[i] * rightArr[i+1]
        
        result = [1 for x in nums]
        for i in range(len(nums)):
            if i == 0:
                result[i] = rightArr[i+1]
            elif i == len(nums)-1:
                result[i] = leftArr[i-1]
            else:
                result[i] = rightArr[i+1] * leftArr[i-1]
        
        return result
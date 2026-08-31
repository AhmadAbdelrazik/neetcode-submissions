class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            j = target-nums[i]
            if j in m:
                return [m[j], i]
            m[nums[i]]=i
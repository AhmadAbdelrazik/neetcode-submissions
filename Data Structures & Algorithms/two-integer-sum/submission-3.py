class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i in range(len(nums)):
            j = target - nums[i]
            if j in m:
                return [m[j], i]
            if nums[i] not in m:
                m[nums[i]] = i
        return []
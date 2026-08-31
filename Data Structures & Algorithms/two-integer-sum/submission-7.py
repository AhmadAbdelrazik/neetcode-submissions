class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = {}
        for i, n in enumerate(nums):
            if target-n in f:
                return [f[target-n], i]

            if n not in f:
                f[n] = i
        
        return []

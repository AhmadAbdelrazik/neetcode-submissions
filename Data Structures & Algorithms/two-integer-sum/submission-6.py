class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, n in enumerate(nums):
            val = target - n
            if val in freq:
                return [freq[val], i]
            freq[n] = i
        return []
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        f = {}
        for num in nums:
            if num not in f:
                f[num] = True
            else:
                return True
        return False
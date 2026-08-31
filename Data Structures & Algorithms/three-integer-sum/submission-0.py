class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            l, r = i + 1, len(nums) -1
            while l < r:
                if a + nums[l] + nums[r] < 0:
                    l += 1
                elif a + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    while l < r and a + nums[l] + nums[r] == 0:
                        l += 1
            
        return res
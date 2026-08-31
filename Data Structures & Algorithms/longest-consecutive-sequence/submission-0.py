class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = True
        
        res = 0
        for n in nums:
            if n-1 in count:
                continue
            l = 1
            while n+l in count:
                l += 1
            if l > res:
                res = l
        
        return res
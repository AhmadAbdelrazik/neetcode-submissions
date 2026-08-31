class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        least = float('inf')
        for n in prices:
            if n < least:
                least = n
            if n - least > res:
                res = n - least
        
        return res

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        highest = 0
        for p in piles:
            highest = max(highest, p)
        
        l, r = 1, highest

        ans = highest
        while l <= r:
            rate = l + ((r - l) // 2) # chosen rate for test
            
            timeTaken = 0
            for p in piles:
                timeTaken += math.ceil(p / rate)
        
            if timeTaken > h:
                l = rate + 1
                continue
            
            ans = min(rate, ans)
            r = rate - 1

        return ans
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # highest value in the pile
        highest = 0
        for pile in piles:
            highest = max(highest, pile)
        
        l, r = 1, highest
        k = -1
        while l <= r:
            m = (l + r) // 2
            hh = 0
            for pile in piles:
                hh += math.ceil(pile / m)
            
            if hh > h:
                l = m + 1
            else:
                k = m
                r = m - 1
        
        return k
        
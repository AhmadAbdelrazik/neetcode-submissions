class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = {}
        for m in s1:
            count[m] = 1 + count.get(m, 0)
        
        l, r = 0, 0
        while r-l+1 < len(s1):
            count[s2[r]] = count.get(s2[r], 0) - 1
            r += 1

        while r < len(s2):
            count[s2[r]] = count.get(s2[r], 0) - 1
            r += 1
            value = 0
            for v in count.values():
                value += abs(v)
            if value == 0:
                return True
            count[s2[l]] += 1
            l += 1
        
        return False
            

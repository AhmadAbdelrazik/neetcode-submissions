class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count = {}
        for m in s1:
            count[m] = 1 + count.get(m, 0)
        
        l, r = 0, 0

        while r < len(s2):
            if r-l == len(s1):
                return True
            if s2[r] not in count:
                while l < r:
                    count[s2[l]] += 1
                    l += 1
                r += 1
                l = r
                continue
            else: 
                count[s2[r]] -= 1
                r += 1
                while count[s2[r-1]] < 0:
                    count[s2[l]] += 1
                    l += 1
        
        if r-l == len(s1):
            return True
        else:
            return False

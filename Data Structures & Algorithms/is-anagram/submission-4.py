class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f = {}
        for ch in s:
            if ch not in f:
                f[ch] = 1
            else:
                f[ch] += 1
        
        for ch in t:
            if ch not in f:
                return False
            
            f[ch] -= 1
        
        for v in f.values():
            if v != 0:
                return False
        
        return True
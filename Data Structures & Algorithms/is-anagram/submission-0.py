class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        
        for ch in t:
            if ch not in freq:
                return False
            else:
                freq[ch] -= 1
        
        for ch, f in freq.items():
            if f != 0:
                return False
        
        return True
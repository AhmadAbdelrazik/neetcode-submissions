class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        freq = {}
        highest = s[0]
        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            if freq[s[r]] > freq[highest]:
                highest = s[r]
            while freq[highest] + k < r-l+1:
                if r-l > res:
                    res = r-l
                freq[s[l]] -= 1
                highestValue = freq[highest]
                for ch, v in freq.items():
                    if v > highestValue:
                        highest = ch
                l += 1
            
            r += 1
        
        if r-l > res:
            res = r-l
        
        return res
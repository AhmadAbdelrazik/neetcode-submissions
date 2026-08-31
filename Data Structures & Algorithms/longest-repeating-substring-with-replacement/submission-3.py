class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        res = 0
        freq = {}
        maxf = 0
        while r < len(s):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            if freq[s[r]] > maxf:
                maxf = freq[s[r]]
            while r-l+1 - maxf > k:
                if r-l > res:
                    res = r-l
                freq[s[l]] -= 1
                l += 1
            r += 1
        
        if r-l > res:
            res = r-l
        
        return res
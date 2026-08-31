class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        m = {}
        while r < len(s):
            m[s[r]] = 1 + m.get(s[r], 0)
            while m[s[r]] > 1:
                if r - l > res:
                    res = r - l
                m[s[l]] -= 1
                l += 1
            r += 1
        
        if r - l > res:
            res = r - l
        
        return res
        
            
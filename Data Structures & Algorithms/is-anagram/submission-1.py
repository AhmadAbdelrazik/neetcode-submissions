class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = ''.join(sorted(s))
        tt = ''.join(sorted(t))
        return ss == tt
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        length = ""
        n = 0
        for i in range(len(s)):
            if n > 0:
                n -= 1
                continue
            if s[i] != '#':
                length += s[i]
            else:
                n = int(length)
                res.append(s[i+1:i+1+n])
                length = ""
        return res
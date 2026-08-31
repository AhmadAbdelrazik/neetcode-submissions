class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        num = ""
        n = 0
        for i in range(len(s)):
            if n > 0:
                n -= 1
                continue
            ch = s[i]
            if ch == "#":
                n = int(num)
                t = s[i+1:i+1+n]
                ans.append(t)
                num = ""
            else:
                num += ch
        
        return ans

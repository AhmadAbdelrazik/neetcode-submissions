class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            l = len(s)           
            ans += str(l) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        print(s)
        if s == "":
            return []
        numStr = ""
        number = 0
        t = ""
        result = []
        for ch in s:
            if number == 0:
                if t != "":
                    result.append(t)
                    t = ""
                if ch != "#":
                    numStr += ch
                else:
                    number = int(numStr)
                    numStr = ""
                    if number == 0:
                        result.append("")
            else:
                t += ch
                number -= 1
        
        if t != "":
            result.append(t)
        return result

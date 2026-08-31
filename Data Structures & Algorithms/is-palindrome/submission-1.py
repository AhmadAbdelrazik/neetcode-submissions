class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for ch in s:
            if "a" <= ch <= "z" or "0" <= ch <= "9":
                t += ch
            elif "A" <= ch <= "Z":
                t += chr(ord(ch) - ord("A") + ord("a"))


            tt = list(t)
            tt.reverse()
            tt = "".join(tt)
    
        return t == tt
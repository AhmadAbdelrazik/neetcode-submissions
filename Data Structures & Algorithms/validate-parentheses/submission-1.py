class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ["[", "(", "{"]:
                stack.append(ch)
            if len(stack) == 0:
                return False
            if ch == "]":
                val = stack.pop()
                if val != "[":
                    return False
            elif ch == ")":
                val = stack.pop()
                if val != "(":
                    return False
            elif ch == "}":
                val = stack.pop()
                if val != "{":
                    return False
        
        return len(stack) == 0

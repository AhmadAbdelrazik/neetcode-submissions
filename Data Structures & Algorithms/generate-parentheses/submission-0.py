class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(s: str, available: int, length: int) -> list[str]:
            if length == 0:
                if available == 0:
                    return [s]
                else:
                    return []

            v1 = rec(s + "(", available + 1, length - 1)
            if available > 0:
                return v1 + rec(s + ")", available - 1, length - 1)
            else:
                return v1
        
        return rec("", 0, n * 2)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                v2 = stack.pop()
                v1 = stack.pop()
                v = v1 + v2
                stack.append(v)
            elif token == "-":
                v2 = stack.pop()
                v1 = stack.pop()
                v = v1 - v2
                stack.append(v)
            elif token == "*":
                v2 = stack.pop()
                v1 = stack.pop()
                v = v1 * v2
                stack.append(v)
            elif token == "/":
                v2 = stack.pop()
                v1 = stack.pop()
                v = int(v1 / v2)
                stack.append(v)
            else:
                stack.append(int(token))

        return stack[-1]
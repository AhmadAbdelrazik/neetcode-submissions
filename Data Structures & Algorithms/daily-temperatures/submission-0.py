class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, n in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < n:
                idx = stack.pop()[1]
                res[idx] = i - idx
            stack.append((n, i))

        return res
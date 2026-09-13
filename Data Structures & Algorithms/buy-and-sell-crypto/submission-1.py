class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        stack = []
        for n in prices:
            while len(stack) > 0 and stack[-1] > n:
                stack.pop()
            stack.append(n)
            res = max(res, stack[-1] - stack[0])
        
        return res
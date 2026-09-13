class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        trapped = 0
        i, j = 0, 1
        while j < len(height):
            if height[j] < height[i]:
                trapped += height[i] - height[j]
            else:
                res += trapped
                trapped = 0
                i = j
            j += 1
        
        trapped = 0
        j, k = len(height)-1, len(height)-2
        while k >= i:
            if height[k] < height[j]:
                trapped += height[j] - height[k]
            else:
                res += trapped
                trapped = 0
                j = k
            k -= 1

        return res
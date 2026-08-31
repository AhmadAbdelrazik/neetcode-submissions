class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        block, total = 0, 0

        while r < len(height):
            if height[r] < height[l]:
                block += height[r]
                r += 1
            else:
                area_between = (r-l-1) * height[l]
                total += area_between - block
                block = 0
                l = r
                r += 1

        block = 0
        r = len(height)-1
        ll = l-1
        l = r-1

        while l > ll:
            if height[l] < height[r]:
                block += height[l]
                l -= 1
            else:
                area_between = (r-l-1) * height[r]
                total += area_between - block
                block = 0
                r = l
                l -= 1

        return total
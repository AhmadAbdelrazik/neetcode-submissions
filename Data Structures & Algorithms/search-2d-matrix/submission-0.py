class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(nums: List[int]) -> bool:
            l, r = 0, len(nums) - 1

            while l <= r:
                m = l + ((r - l) // 2)
                
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return True
            return False

        for nums in matrix:
            found = binary_search(nums)
            if found == True:
                return True

        return False
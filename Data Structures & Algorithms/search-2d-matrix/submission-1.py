class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        i = -1 # the array that might contain the target
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] < target:
                i = m
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                return True

        l, r = 0, len(matrix[i]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[i][m] < target:
                l = m + 1
            elif matrix[i][m] > target:
                r = m - 1
            else:
                return True
        
        return False

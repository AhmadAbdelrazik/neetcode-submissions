class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(numbers)):
            n = numbers[i]
            if target - n in m:
                return [m[target-n]+1, i+1]
            m[n] = i
        
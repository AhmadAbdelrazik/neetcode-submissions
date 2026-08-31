class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        mySet = set()
        for n in nums:
            mySet.add(n)
            
        ans = 1
        for n in mySet:
            if n - 1 in mySet:
                continue
            val = n + 1
            counter = 1
            while val in mySet:
                counter += 1
                val += 1
            if counter > ans:
                ans = counter

        return ans

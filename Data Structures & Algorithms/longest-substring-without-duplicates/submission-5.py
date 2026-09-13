class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        res = 0
        i, j = 0, 0
        while j < len(s):
            if s[j] not in mySet:
                mySet.add(s[j])
            else:
                res = max(res, j-i)
                while s[i] != s[j]:
                    mySet.remove(s[i])
                    i += 1
                i += 1
            j += 1
        
        return max(res, j - i)
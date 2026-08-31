class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        myMap = {}
        for n in s:
            if n not in myMap:
                myMap[n] = 1
            else:
                myMap[n] += 1
        
        for n in t:
            if n not in myMap:
                return False
            else:
                myMap[n] -= 1

        for n in myMap.values():
            if n != 0:
                return False
        return True

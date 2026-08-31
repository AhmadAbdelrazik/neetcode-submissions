class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashMap = dict()
        for s in strs:
            t = ''.join(sorted(s))
            if t in hashMap:
                hashMap[t].append(s)
            else:
                hashMap[t] = [s]
        
        for v in hashMap.values():
            result.append(v)
        return result
                
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        m = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in m:
                m[key].append(s)
            else:
                m[key] = [s]
        
        for v in m.values():
            result.append(v)
        return result
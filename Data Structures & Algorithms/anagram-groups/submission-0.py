class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        m = dict()
        for s in strs:
            t = []
            for ch in s:
                t.append(ch)
            t.sort()
            key = ""
            for ch in t:
                key += ch
            if key in m:
                m[key].append(s)
            else:
                m[key] = [s]
        for v in m.values():
            result.append(v)
        return result

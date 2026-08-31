class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        f = {}
        for st in strs:
            sortedStr = "".join(sorted(st))
            if sortedStr not in f:
                f[sortedStr] = [st]
            else:
                f[sortedStr].append(st)
        
        result = []
        for anagrams in f.values():
            result.append(anagrams)
        
        return result

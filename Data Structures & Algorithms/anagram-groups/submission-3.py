class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            anagram = "".join(sorted(s))
            if anagram not in anagrams:
                anagrams[anagram] = [s]
            else:
                anagrams[anagram].append(s)
        
        res = []
        for n in anagrams.values():
            res.append(n)

        return res
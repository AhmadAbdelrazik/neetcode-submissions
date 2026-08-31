class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = {}
        for n in nums:
            if n not in f:
                f[n] = 1
            else:
                f[n] += 1
        
        m = {}
        arr = []
        for num, freq in f.items():
            if freq not in m:
                arr.append(freq)
                m[freq] = [num]
            else:
                m[freq].append(num)
        
        arr.sort()
        arr.reverse()

        res = []
        for freq in arr:
            res.extend(m[freq])
        
        return res[:k]
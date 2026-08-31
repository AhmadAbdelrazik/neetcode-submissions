class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        
        bucket = [[] for i in range(len(nums) + 1)]
        for n, f in freq.items():
            bucket[f].append(n)
        
        bucket.reverse()
        ans = []
        for n in bucket:
            if len(ans) >= k:
                break
            for v in n:
                ans.append(v)
            
        return ans[:k]

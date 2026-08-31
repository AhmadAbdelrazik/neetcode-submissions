class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        bucket = [[] for x in range(len(nums) + 1)]
        for n, f in count.items():
            bucket[f].append(n)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result
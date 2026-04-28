class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        buckets = {}
        for num, freq in counts.items():
            if freq not in buckets:
                buckets[freq] = []
            buckets[freq].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            if i in buckets:
                for num in buckets[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

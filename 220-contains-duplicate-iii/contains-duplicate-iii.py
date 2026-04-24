class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0: 
            return False
        buckets = {}
        w = valueDiff + 1
        for i, n in enumerate(nums):
            bucket_id = n // w
            if bucket_id in buckets:
                return True
            if (bucket_id - 1) in buckets and abs(n - buckets[bucket_id - 1]) < w:
                return True
            if (bucket_id + 1) in buckets and abs(n - buckets[bucket_id + 1]) < w:
                return True
            buckets[bucket_id] = n
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // w
                del buckets[old_bucket_id]
        return False
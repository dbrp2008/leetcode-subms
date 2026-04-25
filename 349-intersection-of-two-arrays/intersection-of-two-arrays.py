class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashsetnums1 = set(nums1)
        hashsetnums2 = set(nums2)
        return list(hashsetnums1 & hashsetnums2)
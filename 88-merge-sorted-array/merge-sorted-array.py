class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        count_deleted = 0
        while i < len(nums1) and count_deleted < n:
            if nums1[i] == 0:
                del nums1[i]
                count_deleted +=1
            else:
                i += 1

        nums1.extend(nums2)
        nums1.sort()
        """
        Do not return anything, modify nums1 in-place instead.
        """
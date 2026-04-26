class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = {}
        for i in nums1:
            if i not in n1:
                n1[i] = 0
            n1[i] += 1
        final = []
        for i in nums2:
            if n1.get(i,0) != 0:
                final.append(i)
                n1[i] -= 1
        return final

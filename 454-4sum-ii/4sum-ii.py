class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        hash_map = {}
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                summ = nums1[i]+nums2[j]
                hash_map[summ] = hash_map.get(summ, 0) + 1
        for k in range(0, len(nums3)):
            for l in range(0, len(nums4)):
                target = -(nums3[k] + nums4[l])
                if target in hash_map:
                    count += hash_map[target]
        return count
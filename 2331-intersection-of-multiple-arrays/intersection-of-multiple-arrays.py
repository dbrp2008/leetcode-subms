class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hashset = set(nums[0])
        for i in range(1, len(nums)):
            hashset = hashset.intersection(set(nums[i]))    
        return sorted(list(hashset))
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dist = sorted(list(set(nums)))
        if len(dist) >= 3:
            return dist[-3]
        else:
            return dist[-1]
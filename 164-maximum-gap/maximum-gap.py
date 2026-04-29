class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_diff = 0
        if len(nums) < 2:
            return 0
        for i in range(0,len(nums)-1):
            diff = nums[i+1] - nums[i]
            if diff > max_diff:
                max_diff = diff
        return max_diff

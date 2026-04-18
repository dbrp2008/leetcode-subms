class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        leftSum = 0
        for i in range(n):
            leftSum += nums[i]
            rightSum = total - leftSum + nums[i]
            if leftSum == rightSum:
                return i
        return -1

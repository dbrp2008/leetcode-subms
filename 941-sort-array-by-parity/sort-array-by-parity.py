class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(len(nums) -1, -1, -1):
            if nums[i] % 2 != 0:
                odd.append(nums[i])
            if nums[i] % 2 == 0:
                even.append(nums[i])
        return even+odd
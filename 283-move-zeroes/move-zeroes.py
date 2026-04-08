class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        places = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[places] = nums[i]
                places +=1
        for i in range(places, len(nums)):
            nums[i] = 0
        """
        Do not return anything, modify nums in-place instead.
        """
        
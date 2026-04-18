class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        new = sorted(nums)
        max = new[len(new)-1]
        count = 0
        pos = 0
        for i in range(0, len(nums)):
            if max == nums[i]:
                pos = i
            if nums[i] == 0:
                count += 1 
            if nums[i] != 0:
                if max/nums[i] >= 2:
                    count += 1
                if max/nums[i] < 2:
                    count -= 1
        if count == len(nums)-2:
            return pos
        else:
            return -1
        
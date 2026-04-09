class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numsset = set(nums)
        notttherenums = []
        for i in range(1, n+1):
            if i not in numsset:
                notttherenums.append(i)
        return notttherenums
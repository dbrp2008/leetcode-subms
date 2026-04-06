class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final = []
        for i in nums:
            square = i ** 2
            final.append(square)
        final.sort()
        return final
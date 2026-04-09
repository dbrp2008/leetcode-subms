class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        unexpected = 0
        for i in range(0, len(heights)):
            if heights[i] != expected[i]:
                unexpected += 1
        return unexpected
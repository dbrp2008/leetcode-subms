class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        final = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                final.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                final.append(matrix[i][right])
            right -= 1
            if not (top <= bottom and left <= right):
                return final
            for i in range(right, left - 1, -1):
                final.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                final.append(matrix[i][left])
            left += 1
        return final